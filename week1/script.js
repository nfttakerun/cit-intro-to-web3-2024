document.addEventListener('DOMContentLoaded', () => {
    const tableDiv = document.getElementById('multiplication-table');
  
    for (let row = 1; row <= 12; row++) {
      for (let col = 1; col <= 12; col++) {
        const cell = document.createElement('div');
        cell.className = 'cell';
        cell.textContent = row * col;
        tableDiv.appendChild(cell);
      }
    }
  });  