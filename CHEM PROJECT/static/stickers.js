// Sticker images (same sticker can appear multiple times)
const stickers = [
  '/static/stickers/tractor.png',
  '/static/stickers/wheat-plant.png',
  '/static/stickers/soil-ph-meter.png',
  '/static/stickers/dig.png'
];

const container = document.getElementById('sticker-container');
const numberOfStickers = 20; // total scattered stickers

for (let i = 0; i < numberOfStickers; i++) {
    const img = document.createElement('img');
    // Randomly pick any sticker (same sticker can appear multiple times)
    img.src = stickers[Math.floor(Math.random() * stickers.length)];
    img.classList.add('sticker');
    img.style.top = Math.random() * 90 + 'vh';
    img.style.left = Math.random() * 90 + 'vw';
    container.appendChild(img);
}

