    const targetElements = document.querySelectorAll('.contextmenu-target-element');
    const contextMenu = document.getElementById('context-menu');
    const textInput = document.getElementById("id_text");

function MainFunction(event){
    if (event === "Первый пункт"){
        navigator.clipboard.writeText(messageVar.querySelector(".message-text").textContent)
    }else if (event === "Второй пункт"){
        textInput.value = `"${messageVar.textContent}" \n`
        textInput.focus()
    }
}


function OpenMenu(){
    event.preventDefault(); // Отменяем стандартное контекстное меню
    contextMenu.style.display = 'block';
    contextMenu.style.left = event.pageX + 'px';
    contextMenu.style.top = event.pageY + 'px';
    window.messageVar = event.target
}


    for(let i = 0; i < targetElements.length; i++){
        targetElements[i].addEventListener('contextmenu', OpenMenu)
    }


    window.addEventListener('click', function() {
        contextMenu.style.display = 'none'; // Скрываем меню при клике вне его
    });