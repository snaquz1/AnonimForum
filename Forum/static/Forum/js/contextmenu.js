    const targetElements = document.querySelectorAll('.contextmenu-target-element');
    const contextMenu = document.getElementById('context-menu');

    for(let i = 0; i < targetElements.length; i++){
        targetElements[i].addEventListener('contextmenu', function(event) {
        event.preventDefault(); // Отменяем стандартное контекстное меню
        contextMenu.style.display = 'block';
        contextMenu.style.left = event.pageX + 'px';
        contextMenu.style.top = event.pageY + 'px';
    });
    }


    window.addEventListener('click', function() {
        contextMenu.style.display = 'none'; // Скрываем меню при клике вне его
    });