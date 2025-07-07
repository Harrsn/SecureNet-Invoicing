function addItem() {
  const container = document.getElementById("items");
  const div = document.createElement("div");
  div.className = "item";
  div.innerHTML = `
    <input name="description" placeholder="Description" required>
    <input name="qty" type="number" placeholder="Qty" required>
    <input name="price" type="number" step="0.01" placeholder="Unit Price" required>
    <button type="button" onclick="removeItem(this)">Remove</button>
  `;
  container.appendChild(div);
}

function removeItem(button) {
  button.parentElement.remove();
}
