var dragContainer = document.querySelector(".drag-container");
var itemContainers = [].slice.call(
  document.querySelectorAll(".board-column-content")
);
var columnGrids = [];
var boardGrid;
function UpdateStatus(data) {
  const domain = window.location.origin;
  const url = `${domain}/CRM/company/StatusUpdater`;

  const requestOptions = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  };

  fetch(url, requestOptions)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      console.log("Response:", data);
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}
// Init the column grids so we can drag those items around.
itemContainers.forEach(function (container) {
  var grid = new Muuri(container, {
    items: ".board-item",
    dragEnabled: true,
    dragSort: function () {
      return columnGrids;
    },
    dragContainer: dragContainer,
    dragAutoScroll: {
      targets: (item) => {
        return [
          { element: window, priority: 0 },
          { element: item.getGrid().getElement().parentNode, priority: 1 },
        ];
      },
    },
  })
    .on("dragInit", function (item) {
      item.getElement().style.width = item.getWidth() + "px";
      item.getElement().style.height = item.getHeight() + "px";
    })
    .on("dragReleaseEnd", function (item) {
      item.getElement().style.width = "";
      item.getElement().style.height = "";
      item.getGrid().refreshItems([item]);

      console.log(item.getElement().closest(".board-column").id);
      console.log(item.getElement().id);
      const data = {
        Company_id: item.getElement().id,
        Status: item.getElement().closest(".board-column").id,
      };
      UpdateStatus(data);
    })
    .on("layoutStart", function () {
      boardGrid.refreshItems().layout();
    });

  columnGrids.push(grid);
});

// Init board grid so we can drag those columns around.
boardGrid = new Muuri(".board", {
  dragEnabled: true,
  dragHandle: ".board-column-header",
});
