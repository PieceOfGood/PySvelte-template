window.addEventListener("beforeunload", () => {
    py_call("unload");
})
