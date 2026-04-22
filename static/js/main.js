
window.addEventListener("DOMContentLoaded", (event) => {
    input = document.getElementById("search")
    list_items = document.getElementById("list_li")
    input.addEventListener("input", filter)
    function filter() {
        let search = input.value.toString().toLoverCase();

        list_items.forEach(function (li) {
            text = li.innerHTML.toLoverCase()
            found = text.indexOf(search)
            if (search == '') {
                li.style.display = 'block'
            } else if (found == -1) {
                li.style.display = 'none'
            } else {
                li.style.display = 'block'
            }
        });
    }
})