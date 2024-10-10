function filterSpots(status) {
  const spots = document.querySelectorAll(".parking-lot div");
  spots.forEach((spot) => {
    if (status === "free" && spot.classList.contains("free")) {
      spot.style.backgroundColor = "green";
    } else if (status === "occupied" && spot.classList.contains("taken")) {
      spot.style.backgroundColor = "red";
    } else {
      spot.style.backgroundColor = "gray";
    }
  });
}
