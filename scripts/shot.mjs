import { chromium } from 'playwright';

const pages = [
  ['/', 'index'],
  ['/zao/', 'zao'],
  ['/wavewarz/', 'wavewarz'],
  ['/bczyapz/', 'bczyapz'],
  ['/nexus.html', 'nexus'],
  ['/kit.html', 'kit'],
];

const base = process.argv[2] || 'https://bettercallzaal.com';
const browser = await chromium.launch();
const ctx = await browser.newContext({ viewport: { width: 424, height: 900 }, deviceScaleFactor: 2 });
const page = await ctx.newPage();

async function revealAll() {
  await page.evaluate(async () => {
    const step = Math.round(window.innerHeight * 0.8);
    const max = document.body.scrollHeight;
    for (let y = 0; y < max; y += step) {
      window.scrollTo(0, y);
      await new Promise(r => setTimeout(r, 250));
    }
    window.scrollTo(0, 0);
    document.querySelectorAll('.fade-in').forEach(el => {
      el.classList.add('visible');
      el.style.opacity = '1';
      el.style.transform = 'none';
    });
    await new Promise(r => setTimeout(r, 300));
  });
}

for (const [route, name] of pages) {
  try {
    await page.goto(base + route, { waitUntil: 'networkidle', timeout: 30000 });
    await page.waitForTimeout(600);
    await revealAll();
    await page.screenshot({ path: `scripts/shots/${name}-424.png`, fullPage: true });
    console.log(`OK   ${route} -> ${name}-424.png`);
  } catch (e) {
    console.log(`FAIL ${route} : ${e.message}`);
  }
}

await browser.close();
