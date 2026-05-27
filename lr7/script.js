function makeOrder(){

    let cake =
    document.getElementById("cake");

    let cakeName =
    cake.options[cake.selectedIndex].text;

    let cakePrice =
    Number(cake.value);

    let count =
    Number(document.getElementById("count").value);

    let size =
    Number(document.getElementById("size").value);

    let comment =
    document.getElementById("comment").value;

    let total =
    cakePrice * count * size;

    let result =
    document.getElementById("result");

    result.style.display = "block";

    result.innerHTML = `
        <h3>Заказ оформлен 🎂</h3>

        <p><b>Товар:</b> ${cakeName}</p>

        <p><b>Количество:</b> ${count}</p>

        <p><b>Итоговая стоимость:</b> ${total} ₽</p>

        <p><b>Комментарий:</b> ${comment}</p>
    `;
}
