/**
 * BTC Consulting – AI Agent Worker
 * Cloudflare Worker: Claude with WikiChar web tool + BTC knowledge base.
 * Deploy: wrangler deploy
 * Env vars required: ANTHROPIC_API_KEY, LEADS (KV), LEADS_TOKEN
 */

const CORS = {
  'Access-Control-Allow-Origin':  '*',
  'Access-Control-Allow-Methods': 'POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type',
};

// ── Tool: fetch WikiChar or other technical sources ─────────────────────────
const TOOLS = [
  {
    name: 'web_fetch',
    description: 'Fetch content from a URL. Use primarily for WikiChar (https://www.wikichar.net) ' +
      'when you need specific scientific data about hydrochar properties, HTC process parameters, ' +
      'research results, or any other technical reference not in your knowledge base. ' +
      'You can also fetch other scientific or regulatory pages if needed.',
    input_schema: {
      type: 'object',
      properties: {
        url: {
          type: 'string',
          description: 'Full URL to fetch. For WikiChar use e.g. https://www.wikichar.net or specific page URLs.',
        },
      },
      required: ['url'],
    },
  },
];

async function executeTool(name, input) {
  if (name === 'web_fetch') {
    const url = input.url;
    try {
      const res = await fetch(url, {
        headers: {
          'User-Agent': 'BTC-Consulting-Bot/1.0',
          'Accept': 'text/html,application/xhtml+xml,text/plain',
        },
        redirect: 'follow',
      });
      const html = await res.text();
      // Strip scripts, styles, tags; limit to 6000 chars
      const text = html
        .replace(/<script[\s\S]*?<\/script>/gi, '')
        .replace(/<style[\s\S]*?<\/style>/gi, '')
        .replace(/<[^>]+>/g, ' ')
        .replace(/\s+/g, ' ')
        .trim()
        .slice(0, 6000);
      return text || 'Сторінка не містить текстового контенту.';
    } catch (e) {
      return `Помилка при завантаженні ${url}: ${e.message}`;
    }
  }
  return 'Інструмент не знайдено.';
}

// ── Knowledge base / system prompt ──────────────────────────────────────────
const SYSTEM_PROMPT = `
Ти — технічний консультант BTC Consulting (biotc.pl), компанії, що впроваджує
BTC / HTC (Hydrothermal Carbonization) установки для обробки мулу очисних станцій
та промислових підприємств.

НАУКОВІ ДЖЕРЕЛА
Якщо тобі потрібні конкретні дані про властивості гідровугілля, параметри HTC-процесу
або результати досліджень, які не зазначені нижче, використовуй інструмент web_fetch
для звернення до WikiChar — міжнародної бази даних гідровугілля:
  https://www.wikichar.net

ТЕМАТИЧНІ МЕЖІ (КРИТИЧНО ВАЖЛИВО)
Ти відповідаєш ВИКЛЮЧНО на запитання що стосуються:
  - Обробки та утилізації каналізаційного мулу / осадів стічних вод
  - Технологій BTC / HTC / термальної карбонізації
  - Очисних станцій та промислових об'єктів (КОС, харчова промисловість тощо)
  - Директиви UWWTD, екологічного законодавства ЄС щодо водовідведення
  - Фінансування, грантів, окупності проектів з обробки мулу
  - Компанії BTC Consulting та її послуг

Якщо запитання НЕ пов'язане з цими темами — відповідай ТІЛЬКИ:
"Я спеціалізуюсь виключно на питаннях поводження з мулом та технології BTC/HTC.
Якщо у вас є питання по вашому об'єкту — радо допоможу."
Не пояснюй чому не відповідаєш, не вибачайся, не пропонуй альтернатив поза темою.

ТВОЯ РОЛЬ
- Аналізувати описи або завантажені документи (PDF, XLSX) про об'єкти клієнтів.
- Надавати конкретні розрахунки окупності на основі Моделі Уникнутих Витрат.
- Рекомендувати оптимальний сценарій з 5 варіантів поводження з мулом.
- Відповідати українською або польською залежно від мови запиту.
- Бути лаконічним, конкретним, уникати зайвого маркетингу.
- При необхідності використовувати web_fetch для отримання актуальних даних з WikiChar.

═══════════════════════════════════════════════════════════════════
БАЗА ЗНАНЬ — ТЕХНОЛОГІЯ BTC / HTC
═══════════════════════════════════════════════════════════════════

ЩО ТАКЕ HTC / BTC
HTC (Hydrothermal Carbonization) — термохімічний процес при 180–220 °C та 10–25 бар
без доступу кисню. Волога сировина (мул 15–25 % СР) перетворюється на гідровугілля
(hydrochar) та технологічну воду (HTC-ліквор).

Ключові параметри:
- Масове скорочення: ×5 (вихід ~20 % від маси входу за сухою речовиною)
- Немає попереднього сушіння (на відміну від піролізу / спалення)
- HTC-ліквор: у 3× прискорює метаногенез у метантанку → більше біогазу
- Гідровугілля: теплотворність 15–20 МДж/кг (як бурий вугілля)
- Процес безперервний, низьке ТО, модульна конструкція
- Сертифікат End-of-Waste → легальний вихід із «відходів»

BTC = власна назва продукту BTC Consulting (BioThermal Carbonization).

НАУКОВІ ПАРТНЕРИ
- Кафедра теплотехніки та охорони довкілля AGH Kraków
- Мережа WikiChar (https://www.wikichar.net) — міжнародна база даних гідровугілля

КОМЕРЦІЙНИЙ КЕЙС
- Жовтень 2025: MPWiK Lubin (Польща) офіційно купили авторські права на TH-AD-HTC
- Будівництво та пусконалагодження: INTROL S.A. Holding (GPW, Варшава)

═══════════════════════════════════════════════════════════════════
ФОРМУЛИ РОЗРАХУНКУ
═══════════════════════════════════════════════════════════════════

Базові зв'язки:
  Volume (т/рік) = PE × 0.1   (1 р.е. = 0.1 т сухого мулу/рік)
  Площа (м²) = Volume × 1.5   (шари сушіння + санітарна зона)
  Площа (соток) = Площа(м²) / 100

CapEx:
  CapEx_total = Volume × 250 €     (~€250 на 1 т/рік потужності)
  Частка міста = CapEx_total × (1 − Грант/100)

ROI:
  Земельний актив = Площа(м²) × (Ціна 1 сотки / 100)
  ROI (роки) = (Частка_міста − Земельний_актив) / Щорічна_економія

═══════════════════════════════════════════════════════════════════
5 СЦЕНАРІЇВ ПОВОДЖЕННЯ З МУЛОМ
═══════════════════════════════════════════════════════════════════

1. МУЛОВІ ПОЛЯ
   f1 = 40–80 €/т (утилізація + вивіз)
   f2 = 20–50 €/т (рекультивація)
   Щорічна економія = V × (f1 + f2)

2. ЦЕНТРИФУГИ + АГРО
   f1 = 60–100 €/т (флокулянти)
   f2 = 20–60 €/т (логістика + виплати фермерам)
   Щорічна економія = V × f1 + V × 0.8 × f2

3. КОМПОСТУВАННЯ
   f1 = 30–80 €/т (тріска / структуроутворювач)
   f2 = 30–60 €/т (операційні витрати)
   Щорічна економія = V × (f1 + f2)

4. СУШІННЯ + СПАЛЕННЯ
   f1 = 60–120 €/т (газ для сушарки)
   f2 = 80–160 €/т сухого залишку (Gate Fee інсинератора)
   Щорічна економія = V×f1 + V×0.2×f2 + біогаз дохід

5. ПОЛІГОН ТПВ
   f1 = 40–120 €/т (екоподаток)
   EU ETS може додати €50–100/т до 2030

═══════════════════════════════════════════════════════════════════
ДИРЕКТИВА UWWTD 2024/3019 (ЄС)
═══════════════════════════════════════════════════════════════════

Дедлайни для очисних станцій:
  PE > 150 000 → 2033  (четвертинне очищення)
  PE > 10 000  → 2036  (третинне очищення)
  PE > 1 000   → 2039  (вторинне очищення)

═══════════════════════════════════════════════════════════════════
ГРАНТИ ТА ФІНАНСУВАННЯ
═══════════════════════════════════════════════════════════════════

  EU LIFE Programme: 60–75 % CapEx
  Horizon Europe: до 100 % R&D
  KRPOiŚ (Польща): до 85 %
  Ukrainian Recovery Fund: до 80 %
  ЄБРР / КЕБ: пільгові кредити 15–25 років
  Типове припущення в моделі: 75 % грант

═══════════════════════════════════════════════════════════════════
ТИПОВІ ОБ'ЄКТИ
═══════════════════════════════════════════════════════════════════

Комунальні (КОС):
  Містечко/Gmina:    ~20 000 PE   →  2 000 т/рік
  Місто:            ~100 000 PE   → 10 000 т/рік
  Агломерація:      ~300 000 PE   → 30 000 т/рік

Промислові:
  Пивзавод (~2M гл/рік):   60 000 PE eq.  →  6 000 т/рік
  Цукрозавод (~8000 т буряка/день):  25 000 PE eq.
  М'ясокомбінат (~500 т/день):       50 000 PE eq.
  Молокозавод (~500 т/день):         30 000 PE eq.

═══════════════════════════════════════════════════════════════════
ФОРМАТ ВІДПОВІДІ
═══════════════════════════════════════════════════════════════════

Коротко (≤ 3 речення): якщо питання просте або вступне.
Структуровано (блоки з цифрами): якщо є конкретні дані об'єкту.

При наявності даних — завжди надавай:
  • Рекомендований сценарій та чому
  • Щорічну економію (€/рік)
  • Орієнтовний CapEx та частку міста/компанії після гранту
  • ROI (роки) або "Миттєва" якщо земля перекриває витрати
  • Наступний крок: "Замовте безкоштовну інженерну оцінку"

Якщо запит потребує виїзду або точних розрахунків — скеровуй до:
  contact@biotc.pl | +48 608 003 458
`.trim();

// ── CSV helpers ───────────────────────────────────────────────────────────────
const CSV_HEADER = 'ts,session_id,scenario,vol_ty,vol_pe,grant,f1,f2,capex_total,capex_city,savings,land,roi\n';

function leadToRow(d) {
  return [d.ts, d.session_id, d.scenario, d.vol_ty, d.vol_pe, d.grant,
          d.f1, d.f2, d.capex_total, d.capex_city, d.savings, d.land, d.roi]
    .map(v => (String(v ?? '').includes(',') ? `"${v}"` : (v ?? '')))
    .join(',') + '\n';
}

// ── Stream final response ─────────────────────────────────────────────────────
async function streamResponse(messages, env) {
  const resp = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
      'x-api-key': env.ANTHROPIC_API_KEY,
      'anthropic-version': '2023-06-01',
      'anthropic-beta': 'pdfs-2024-09-25',
      'content-type': 'application/json',
    },
    body: JSON.stringify({
      model: 'claude-sonnet-4-5',
      max_tokens: 2048,
      system: SYSTEM_PROMPT,
      messages,
      tools: TOOLS,
      stream: true,
    }),
  });
  if (!resp.ok) throw new Error(await resp.text());
  return resp;
}

// ── Non-streaming call to check for tool use ──────────────────────────────────
async function callWithTools(messages, env) {
  const resp = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
      'x-api-key': env.ANTHROPIC_API_KEY,
      'anthropic-version': '2023-06-01',
      'anthropic-beta': 'pdfs-2024-09-25',
      'content-type': 'application/json',
    },
    body: JSON.stringify({
      model: 'claude-sonnet-4-5',
      max_tokens: 2048,
      system: SYSTEM_PROMPT,
      messages,
      tools: TOOLS,
    }),
  });

  if (!resp.ok) throw new Error(await resp.text());
  const result = await resp.json();

  if (result.stop_reason === 'tool_use') {
    // Execute each tool call
    const toolResults = [];
    for (const block of result.content) {
      if (block.type === 'tool_use') {
        const output = await executeTool(block.name, block.input);
        toolResults.push({
          type: 'tool_result',
          tool_use_id: block.id,
          content: output,
        });
      }
    }

    // Build messages with tool results and stream final response
    const newMessages = [
      ...messages,
      { role: 'assistant', content: result.content },
      { role: 'user',      content: toolResults },
    ];

    return streamResponse(newMessages, env);
  }

  // No tool use — stream directly
  return streamResponse(messages, env);
}

// ── Main handler ─────────────────────────────────────────────────────────────
export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (request.method === 'OPTIONS') {
      return new Response(null, { status: 204, headers: CORS });
    }

    // ── POST /lead ────────────────────────────────────────────────────────────
    if (request.method === 'POST' && url.pathname === '/lead') {
      let lead;
      try { lead = await request.json(); } catch { return json({ error: 'bad json' }, 400); }
      if (env.LEADS) {
        const key = `lead:${lead.ts || Date.now()}:${Math.random().toString(36).slice(2)}`;
        await env.LEADS.put(key, JSON.stringify(lead));
      }
      return json({ ok: true });
    }

    // ── GET /leads.csv ────────────────────────────────────────────────────────
    if (request.method === 'GET' && url.pathname === '/leads.csv') {
      const token = url.searchParams.get('token');
      if (!env.LEADS_TOKEN || token !== env.LEADS_TOKEN) {
        return new Response('Unauthorized', { status: 401 });
      }
      const list = await env.LEADS.list({ prefix: 'lead:' });
      let csv = CSV_HEADER;
      for (const key of list.keys) {
        const raw = await env.LEADS.get(key.name);
        if (raw) { try { csv += leadToRow(JSON.parse(raw)); } catch {} }
      }
      return new Response(csv, {
        headers: { 'content-type': 'text/csv; charset=utf-8',
                   'content-disposition': 'attachment; filename="btc-leads.csv"', ...CORS },
      });
    }

    if (request.method !== 'POST') {
      return new Response('Method Not Allowed', { status: 405 });
    }

    let body;
    try { body = await request.json(); }
    catch { return json({ error: 'Invalid JSON' }, 400); }

    const { messages = [], file } = body;
    if (!messages.length) return json({ error: 'No messages' }, 400);

    // Build Anthropic messages array
    const anthropicMessages = messages.map((m, i) => {
      if (file && i === messages.length - 1 && m.role === 'user') {
        const content = [];
        if (file.type === 'application/pdf' || file.type?.startsWith('image/')) {
          content.push({
            type: file.type.startsWith('image/') ? 'image' : 'document',
            source: { type: 'base64', media_type: file.type, data: file.data },
          });
        }
        content.push({ type: 'text', text: m.content });
        return { role: 'user', content };
      }
      return { role: m.role, content: m.content };
    });

    try {
      const apiResp = await callWithTools(anthropicMessages, env);

      return new Response(apiResp.body, {
        status: 200,
        headers: {
          'content-type': 'text/event-stream; charset=utf-8',
          'cache-control': 'no-cache',
          ...CORS,
        },
      });
    } catch (err) {
      return json({ error: err.message }, 500);
    }
  },
};

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'content-type': 'application/json', ...CORS },
  });
}
