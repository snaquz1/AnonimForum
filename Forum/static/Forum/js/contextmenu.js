    const targetElements = document.querySelectorAll('.contextmenu-target-element');
    const contextMenu = document.getElementById('context-menu');
    const textInput = document.getElementById("id_text");
    const submitBtn = document.getElementById("submit_btn");

    window.scrollTo(0, document.body.scrollHeight)

function MainFunction(event){
    if (event === "Первый пункт"){
        navigator.clipboard.writeText(messageVar.querySelector(".message-text").textContent)
    }else if (event === "Второй пункт"){
        textInput.value = `"${messageVar.textContent}" \n`
        textInput.focus()
    }
}

textInput.addEventListener("keyup", function (){
    if (event.keyCode === 13){
        submitBtn.click()
    }
})


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

