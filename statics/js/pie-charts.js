<script src="https://cdn.jsdelivr.net/npm/chart.js@2.9.3/dist/Chart.min.js"></script>
<script>
    var config = {
      type: 'pie',
      data: {
        datasets: [{
          data: [1780000, 1630000, 582602, 416522, 411634, 318332, 318332, 306659, 233040],
          backgroundColor: [
            '#ff0000', '#0000ff', '#ff0080', '#73ffff', '#5c26ff', '#002db3', '#ffff26', '#4cff4c', '#ff00ff'
          ],
          label: 'Population'
        }],
        labels: ['Manila City', 'Davao City', 'Makati', 'Pasay City', 'Angeles City', 'Tarlac City', 'Malolos', 'San Fernando', 'Olongapo City']
      },
      options: {
        responsive: true
      }
    };

    window.onload = function() {
      var ctx = document.getElementById('pie-chart').getContext('2d');
      window.myPie = new Chart(ctx, config);
    };
</script>