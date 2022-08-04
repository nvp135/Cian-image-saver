# Cian-image-saver
Python script 

1. Промотать всю карусель фотографий
2. Вставить в консоль JS скрипт
```
let imgs = document.querySelectorAll("ul > li > img");
let imgSrc = "";
for (var i = 0; i < imgs.length; i++) {
  imgSrc += "\"" + imgs[i].src.replace("-2.jpg", "-1.jpg") + "\",";
}  
console.log(imgSrc);
```
3. Скопировать ссылки из консоли браузера в массив IMG_LINKS
4. Запустить скрипт
