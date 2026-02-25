(function () {
  const toast = document.getElementById('toast');

  function showToast(message) {
    if (!toast) return;
    toast.textContent = message;
    toast.style.opacity = '1';
    setTimeout(() => {
      toast.style.opacity = '0';
    }, 1200);
  }

  document.querySelectorAll('[data-copy]').forEach((btn) => {
    btn.addEventListener('click', async () => {
      const value = btn.getAttribute('data-copy') || '';
      try {
        await navigator.clipboard.writeText(value);
        showToast('Copié !');
      } catch (_) {
        showToast('Copie impossible');
      }
    });
  });
})();