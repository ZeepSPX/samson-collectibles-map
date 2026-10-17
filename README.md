# Samson — карта колекцій / collectibles map

**Українська** · [English](#english)

**Демо / Live demo:** https://zeepspx.github.io/samson-collectibles-map/

---

## Українська

Інтерактивна карта колекційних предметів гри **Samson**: 194 сендвіч-борди, 22 автомобільні журнали та 15 журналів з бойових мистецтв. Позначайте зібране, прогрес зберігається у браузері.

### Як користуватися

- Клік або дотик по маркеру позначає предмет зібраним, повторний клік знімає позначку.
- Внизу показуються номер предмета та його ігрові координати X/Y/Z.
- Панель зліва: лічильники, фільтри за типом, «Сховати зібране», пошук за номером.
- Масштаб: колесо миші, щипок або кнопки «+» і «−». Перетягуйте карту, щоб рухатись.
- **Групування.** Близькі предмети зливаються в кружок із числом. Колір кружка: помаранчевий — самі борди, синій — авто-журнали, червоний — бойові, темний — суміш. Зелена дуга показує, яка частка групи вже зібрана.
  - Клік по групі наближає карту до місця, де вона розпадається.
  - Якщо предмети стоять так близько, що навіть максимальний масштаб їх не розділяє, відкривається список із кнопками «Зібрано» та «Позначити всі зібраними». Закрити його можна клавішею Esc.
  - Вимкнути групування можна галочкою «Групувати близькі предмети».
- **Прогрес** запам'ятовується у браузері (`localStorage`). Для переносу між пристроями є кнопки «Зберегти у файл» і «Завантажити з файлу» (JSON).
- **Мова.** Інтерфейс доступний українською та англійською. Перемикайте кнопкою UA/EN у панелі; вибір запам'ятовується, а за замовчуванням береться мова браузера.
- Номери предметів внутрішні: вони взяті з порядку в `data/collectibles.csv`, у самій грі їх немає.

Сайт повністю статичний: `index.html` містить карту, дані й код, зовнішніх запитів немає. Той самий файл можна просто відкрити з диска й користуватися без інтернету.

### Звідки дані

- **Координати** предметів виписані з експорту рівня гри (World Partition, Unreal Engine): `InventoryItemPickupSpawner` для журналів (`Item_CarMagazine`, `Item_CombatMagazine`) і `SmashableCollectibleSpawner` (`Item_SandwichBoard`) для бордів. Це координати з прототипного рівня, у фінальній версії гри вони можуть відрізнятися.
- **Фонова карта** зібрана з SDF-текстур інтерфейсу гри (вода, вулиці, шосе, парки). Повна карта охоплює квадрат 480 000 × 480 000 одиниць із центром (-32216, -35310):
  - `u = 0.5 + (X + 32216) / 480000`
  - `v = 0.5 + (Y + 35310) / 480000`
- Місце знаходження було перевірено вручну з відомими гайдами журналів.
- Назви районів розставлені на око й наближені.

### Відомі обмеження

- Максимальний масштаб ×2.5, далі фонова карта розмивається.
- Деякі предмети стоять майже в одній точці; їх завжди показує група, а позначати їх можна зі списку.
- Зелені ділянки за межами міста на фоновій карті не відтворені.

### Авторство

Фонову карту та аналіз файлів гри (вилучення координат і побудову карти) виконано за допомогою [Claude](https://claude.ai) від Anthropic.

### Ліцензія і застереження

Код розповсюджується за ліцензією [MIT](LICENSE). Це неофіційний фанатський проєкт, не пов'язаний із розробником і видавцем гри. Samson розроблено й видано студією [Liquid Swords AB](https://www.liquidswords.com/) (гра в [Steam](https://store.steampowered.com/app/3634520/Samson/) і [Epic Games Store](https://store.epicgames.com/p/samson-ab5af7)); назва гри, [Liquid Swords](https://www.liquidswords.com/) і пов'язані матеріали належать їй. Фонова карта, координати та фонове зображення сторінки (офіційний промо-шпалер гри) виведені з матеріалів гри, і ліцензія MIT на них не поширюється.

---

## English

An interactive map of collectibles in the game **Samson**: 194 sandwich boards, 22 car magazines and 15 martial arts magazines. Mark what you have found; progress is saved in your browser.

### How to use

- Click or tap a marker to mark the item as collected; click again to unmark it.
- The bottom bar shows the item number and its in-game X/Y/Z coordinates.
- Left panel: counters, filters by type, "Hide collected", search by number.
- Zoom with the mouse wheel, pinch, or the "+" and "−" buttons. Drag the map to move around.
- **Grouping.** Nearby items merge into a circle with a number. Circle colour: orange — boards only, blue — car magazines, red — martial arts magazines, dark — a mix. The green arc shows how much of the group is already collected.
  - Clicking a group zooms in to the point where it breaks apart.
  - If items are so close that even maximum zoom cannot separate them, a list opens with "Collected" and "Mark all as collected" buttons. Press Esc to close it.
  - Grouping can be turned off with the "Group nearby items" checkbox.
- **Progress** is stored in the browser (`localStorage`). To move it between devices, use the "Save to file" and "Load from file" buttons (JSON).
- **Language.** The interface is available in Ukrainian and English. Use the UA/EN button in the panel; the choice is remembered, and by default it follows your browser language.
- Item numbers are internal: they follow the row order in `data/collectibles.csv` and do not exist in the game itself.

The site is fully static: `index.html` contains the map, data and code, with no external requests. The same file can be opened from disk and used offline.

### Data sources

- **Coordinates** were extracted from the game's level export (World Partition, Unreal Engine): `InventoryItemPickupSpawner` for magazines (`Item_CarMagazine`, `Item_CombatMagazine`) and `SmashableCollectibleSpawner` (`Item_SandwichBoard`) for boards. These are coordinates from a prototype level and may differ in the final version of the game.
- **Background map** was assembled from the game's UI SDF textures (water, streets, highways, parks). The full map covers a 480,000 × 480,000 unit square centred on (-32216, -35310):
  - `u = 0.5 + (X + 32216) / 480000`
  - `v = 0.5 + (Y + 35310) / 480000`
- Locations were checked manually against known magazine guides.
- District names are placed by eye and are approximate.

### Known limitations

- Maximum zoom is ×2.5; beyond that the background map becomes blurry.
- Some items stand almost at the same point; they are always shown as a group, and can be marked from the list.
- Green areas outside the city are not reproduced on the background map.

### Credits

The background map and the analysis of the game files (extracting coordinates and building the map) were made with the help of [Claude](https://claude.ai) by Anthropic.

### License and disclaimer

The code is released under the [MIT](LICENSE) license. This is an unofficial fan project, not affiliated with the game's developer or publisher. Samson is developed and published by [Liquid Swords AB](https://www.liquidswords.com/) (the game on [Steam](https://store.steampowered.com/app/3634520/Samson/) and the [Epic Games Store](https://store.epicgames.com/p/samson-ab5af7)); the game's name, Liquid Swords and related materials belong to them. The background map, coordinates and the page background image (official promotional wallpaper) come from the game's materials, and the MIT license does not cover them.
