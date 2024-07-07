function classtoggle(ClassName) {
    cls = '.' + ClassName
    obj = document.querySelectorAll(cls)
    obj.forEach((element) => {
        element.classList.toggle("d-none")
    });
}