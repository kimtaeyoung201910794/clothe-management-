var backToTop = () => {
    // Scroll | button show/hide
    window.addEventListener('scroll', () => {
      if (document.querySelector('html').scrollTop > 100) {
        document.getElementById('totop_btn').style.display = "block";
      } else {
        document.getElementById('totop_btn').style.display = "none";
      }
    });
    // back to top
    document.getElementById('totop_btn').addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        left: 0,
        behavior: 'smooth'
      });
    })
  };
  backToTop();