function changeView(data, className) {
  var otherName =
    className == "createRequest" ? "viewRequest" : "createRequest";
  var element = document.querySelector(`div.${className}`);
  var Secondelement = document.querySelector(`div.${otherName}`);
  element.style.display = "block";
  Secondelement.style.display = "none";
  var navElement = document.querySelector(`#${otherName}`);
  navElement.classList.remove("active");
  data.classList.add("active");
}
