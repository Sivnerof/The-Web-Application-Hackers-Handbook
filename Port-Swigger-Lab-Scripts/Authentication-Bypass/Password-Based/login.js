function jsonSubmit(loginPath) {
    const formToJSON = elements => [].reduce.call(elements, (data, element) => {
        if (element.name && element.name.length > 0) {
            data[element.name] = element.value;
        }
        return data;
    }, {});

    const jsonObject = formToJSON(document.getElementsByClassName("login-form")[0].elements)
    const formData = JSON.stringify(jsonObject);
    fetch(
        loginPath,
        {
            method: "POST",
            body: formData
        }
    )
        .then(response => {
            response.text().then(t => {
                document.open();
                document.write(t);
                document.close();
            });

            if (response.redirected) {
                history.pushState({}, "", response.url)
            }
        });
}