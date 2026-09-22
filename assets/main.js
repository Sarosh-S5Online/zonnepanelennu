(function () {
  var nav = document.querySelector('nav');
  var burger = document.querySelector('.burger');
  if (burger) burger.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    burger.setAttribute('aria-expanded', open);
  });
  document.querySelectorAll('nav a').forEach(function (a) {
    a.addEventListener('click', function () { nav.classList.remove('open'); });
  });

  // Formulier-koppeling: vul hier de Web3Forms access key van de klant in (of een andere endpoint).
  var CFG = window.ZNN_FORM || { accessKey: '', endpoint: 'https://api.web3forms.com/submit' };
  window.dataLayer = window.dataLayer || [];

  function valid(fields) {
    var ok = true;
    fields.forEach(function (f) {
      var bad = (f.type === 'checkbox') ? !f.checked
        : !f.value.trim() || (f.type === 'email' && !/^\S+@\S+\.\S+$/.test(f.value));
      f.classList.toggle('err', bad);
      if (bad && ok) { f.focus(); ok = false; }
    });
    return ok;
  }

  // Hero: postcode meenemen naar het offerteformulier
  document.querySelectorAll('[data-pc]').forEach(function (box) {
    var input = box.querySelector('input');
    function go() {
      if (!input.value.trim()) { input.classList.add('err'); input.focus(); return; }
      input.classList.remove('err');
      var target = document.getElementById('f-postcode');
      if (target) target.value = input.value;
      var offer = document.getElementById('offerte');
      if (offer) offer.scrollIntoView({ behavior: 'smooth' });
      var first = document.getElementById('f-naam');
      if (first) setTimeout(function () { first.focus({ preventScroll: true }); }, 700);
    }
    box.querySelector('button').addEventListener('click', go);
    input.addEventListener('keydown', function (e) { if (e.key === 'Enter') { e.preventDefault(); go(); } });
  });

  // Offerteformulier
  document.querySelectorAll('[data-form]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!valid([].slice.call(form.querySelectorAll('[required]')))) return;
      var btn = form.querySelector('button[type=submit]');
      var label = btn.textContent; btn.disabled = true; btn.textContent = 'Versturen…';
      function ok() {
        window.dataLayer.push({ event: 'lead_submit', form: 'offerte' });
        form.querySelector('.fields').style.display = 'none';
        form.querySelector('.done').style.display = 'block';
        setTimeout(function () { location.href = '/bedankt/'; }, 900);
      }
      function fail() {
        btn.disabled = false; btn.textContent = label;
        alert('Versturen is niet gelukt. Bel ons gerust op 0182 – 60 79 48.');
      }
      if (!CFG.accessKey) return ok();             // demo-modus: geen backend gekoppeld
      var v = function (id) { return (document.getElementById(id) || {}).value || ''; };
      var data = new FormData();
      data.append('access_key', CFG.accessKey);
      data.append('subject', 'Nieuwe dakscan-aanvraag via zonnepanelennu.nl');
      data.append('from_name', 'ZonnepanelenNu website');
      data.append('naam', v('f-naam')); data.append('telefoon', v('f-tel')); data.append('email', v('f-mail'));
      data.append('postcode_huisnummer', v('f-postcode')); data.append('type_dak', v('f-dak')); data.append('opmerking', v('f-opm'));
      data.append('pagina', location.pathname);
      fetch(CFG.endpoint, { method: 'POST', body: data }).then(function (r) { return r.json(); })
        .then(function (j) { j.success ? ok() : fail(); }).catch(fail);
    });
  });

  // Blog: zoeken + categorie
  var posts = [].slice.call(document.querySelectorAll('#posts .post'));
  if (posts.length) {
    var q = document.querySelector('[data-filter]'), cat = 'Alle', none = document.getElementById('nores');
    function apply() {
      var t = q.value.trim().toLowerCase(), n = 0;
      posts.forEach(function (p) {
        var show = (cat === 'Alle' || p.dataset.cat === cat) && (!t || p.dataset.t.indexOf(t) > -1);
        p.hidden = !show; if (show) { n++; p.classList.add('in'); }
      });
      none.style.display = n ? 'none' : 'block';
    }
    q.addEventListener('input', apply);
    document.querySelectorAll('[data-chip]').forEach(function (c) {
      c.addEventListener('click', function () {
        document.querySelectorAll('[data-chip]').forEach(function (x) { x.classList.remove('on'); });
        c.classList.add('on'); cat = c.dataset.chip; apply();
      });
    });
  }

  // Cookiebanner (koppel later aan Google Consent Mode / GTM)
  var box = document.getElementById('cookie');
  function stored() { try { return localStorage.getItem('znn-consent'); } catch (e) { return null; } }
  function choose(v) {
    try { localStorage.setItem('znn-consent', v); } catch (e) {}
    box.hidden = true;
    window.dataLayer.push({ event: 'consent_update', consent: v === 'yes' ? 'granted' : 'denied' });
  }
  if (box) {
    if (!stored()) box.hidden = false;
    box.querySelectorAll('[data-consent]').forEach(function (b) {
      b.addEventListener('click', function () { choose(b.dataset.consent); });
    });
    document.querySelectorAll('[data-cookie-settings]').forEach(function (a) {
      a.addEventListener('click', function (e) { e.preventDefault(); box.hidden = false; });
    });
  }

  // Batterijcalculator (indicatief; zie de toelichting onder de uitkomst)
  var calcRoot = document.getElementById('calculator');
  if (calcRoot) {
    var $ = function (id) { return document.getElementById(id); };
    var fmtInt = function (n) { return Math.round(n).toLocaleString('nl-NL'); };
    var fmtEuro = function (n) { return '€ ' + fmtInt(n); };
    var fmtKwh = function (n) { return n.toLocaleString('nl-NL', { minimumFractionDigits: 1, maximumFractionDigits: 1 }); };

    var PV_PER_KWP = 950;     // kWh/kWp/jaar, gemiddelde Nederlandse zoninstraling
    var WP_PER_PANEEL = 400;  // ± Wp per paneel
    var PRIJS_IN = 0.28;      // € per ingekochte kWh (indicatief)
    var PRIJS_TERUG = 0.08;   // terugleververgoeding per kWh (indicatief, na saldering)
    var TIERS = [
      { kwh: 4.8, model: 'AEG Solarcube 4,8 kWh' },
      { kwh: 9.6, model: 'AEG Solarcube 9,6 kWh' },
      { kwh: 14.4, model: 'AEG Solarcube 14,4 kWh' }
    ];

    function calc() {
      var verbruik = parseFloat($('c-verbruik').value);
      var kwp = parseFloat($('c-kwp').value);
      var ev = $('c-ev').checked, wp = $('c-wp').checked, dyn = $('c-dyn').checked, btw = $('c-btw').checked;

      $('cv-verbruik').textContent = fmtInt(verbruik) + ' kWh';
      $('cv-kwp').textContent = kwp.toLocaleString('nl-NL', { minimumFractionDigits: 1, maximumFractionDigits: 1 }) + ' kWp';
      var panelen = Math.max(1, Math.round((kwp * 1000) / WP_PER_PANEEL));
      $('cv-panelen').textContent = kwp > 0 ? ('≈ ' + panelen + ' panelen (± ' + WP_PER_PANEEL + ' Wp per paneel)') : 'Nog geen zonnepanelen';

      var pvOpbrengst = kwp * PV_PER_KWP;
      var zelfverbruikAandeel = 0.30;
      var extraJaarverbruik = (ev ? 1200 : 0) + (wp ? 1500 : 0);
      var avondbehoefte = (verbruik * (1 - zelfverbruikAandeel) * 0.6) + extraJaarverbruik;
      var overschot = Math.max(0, pvOpbrengst - (verbruik * zelfverbruikAandeel));
      var bruikbaar = Math.min(overschot, avondbehoefte);

      var ruweCapaciteit = bruikbaar / 280; // effectieve volle-cyclusdagen per jaar (NL-klimaat)
      if (dyn) ruweCapaciteit *= 1.15;      // dynamisch contract: iets grotere batterij is de moeite waard
      var tier = TIERS[0];
      for (var i = 0; i < TIERS.length; i++) { if (ruweCapaciteit > TIERS[i].kwh * 0.75) tier = TIERS[i]; }
      var grootVerbruik = ruweCapaciteit > TIERS[2].kwh * 1.15;

      var extraZelfverbruik = Math.min(bruikbaar, tier.kwh * 300);
      var besparing = extraZelfverbruik * (PRIJS_IN - PRIJS_TERUG);
      if (dyn) besparing += tier.kwh * 0.7 * 60; // indicatieve prijsarbitrage, zie ook het voorbeeld bij "Slim handelen"

      var investeringExcl = 2200 + tier.kwh * 580;
      var investeringNetto = btw ? investeringExcl : investeringExcl * 1.21;
      var terugverdientijd = besparing > 0 ? investeringNetto / besparing : 0;

      $('co-kwh').textContent = fmtKwh(tier.kwh);
      $('co-model').textContent = tier.model + (grootVerbruik ? ' (of groter — bespreken we in het adviesgesprek)' : '');
      $('co-besparing').textContent = fmtEuro(besparing) + ' / jaar';
      var terugStr = '–';
      if (terugverdientijd > 0 && terugverdientijd <= 25) terugStr = terugverdientijd.toLocaleString('nl-NL', { minimumFractionDigits: 1, maximumFractionDigits: 1 }) + ' jaar';
      else if (terugverdientijd > 25) terugStr = 'Nog niet rendabel';
      $('co-terug').textContent = terugStr;
      $('co-investering').textContent = fmtEuro(investeringNetto);
    }

    ['c-verbruik', 'c-kwp', 'c-ev', 'c-wp', 'c-dyn', 'c-btw', 'c-or', 'c-aan'].forEach(function (id) {
      var el = $(id);
      if (el) el.addEventListener('input', calc);
    });
    calc();
  }

  // Scroll-reveal
  var items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: .1 });
    items.forEach(function (i) { io.observe(i); });
  } else items.forEach(function (i) { i.classList.add('in'); });
})();
