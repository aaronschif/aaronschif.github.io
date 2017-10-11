const puppeteer = require('puppeteer');

(async() => {

const browser = await puppeteer.launch();
const page = await browser.newPage();
await page.goto('http://0.0.0.0:8000/resume', {waitUntil: 'networkidle'});
await page.pdf({
    path: `${__dirname}/build/aaron_schif_resume.pdf`,
    format: 'Letter',
    margin: {
            top: '.5cm',
            bottom: '.5cm',
            right: '.5cm',
            left: '.5cm',
        }
    });

browser.close();
})();
