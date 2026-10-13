/* Pathum Thani minisite: lotus pond, Rangsit canals, Sam Khok jar, openbill storks, boat noodles. Every drawing answers a tap. */
(function () {
  'use strict';
  var TH = document.documentElement.lang === 'th';
  var RM = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var T = function (en, th) { return TH ? th : en; };
  var TAU = Math.PI * 2;

  function fit(cv) {
    var r = cv.getBoundingClientRect(), d = Math.min(window.devicePixelRatio || 1, 2);
    cv.width = Math.round(r.width * d); cv.height = Math.round(r.height * d);
    var c = cv.getContext('2d'); c.setTransform(d, 0, 0, d, 0, 0);
    return { c: c, w: r.width, h: r.height };
  }
  function pt(cv, e) { var r = cv.getBoundingClientRect(); return { x: e.clientX - r.left, y: e.clientY - r.top }; }
  function rnd(a, b) { return a + Math.random() * (b - a); }
  function seeded(s) { return function () { s = (s * 16807) % 2147483647; return (s - 1) / 2147483646; }; }
  function bkkHour() { var d = new Date(); return (d.getUTCHours() + 7 + d.getUTCMinutes() / 60) % 24; }
  function loop(fn, cv) {
    var on = true, last = 0;
    if ('IntersectionObserver' in window) new IntersectionObserver(function (e) { on = e[0].isIntersecting; if (on) requestAnimationFrame(tick); }).observe(cv);
    function tick(t) { if (!on) return; var dt = Math.min(0.05, (t - (last || t)) / 1000); last = t; fn(dt, t / 1000); requestAnimationFrame(tick); }
    requestAnimationFrame(tick);
  }

  /* ---------------------------------------------------------------- lotus */
  function lotus(c, x, y, s, open, hue) {
    // side view of Nelumbo nucifera: three rings of petals opening outward, seed pod when open
    var rings = [[7, 1.0, 0.95], [5, 0.82, 0.6], [3, 0.66, 0.25]];
    c.save(); c.translate(x, y); c.scale(s, s);
    rings.forEach(function (ring, ri) {
      var n = ring[0], len = 34 * ring[1], spread = (0.25 + open * ring[2] * 1.15);
      for (var k = 0; k < n; k++) {
        var f = n === 1 ? 0 : k / (n - 1) - 0.5, a = f * spread * 2;
        c.save(); c.rotate(a);
        var g = c.createLinearGradient(0, 0, 0, -len);
        g.addColorStop(0, '#fff6f8'); g.addColorStop(0.55, hue || '#f39ab8'); g.addColorStop(1, '#d9306f');
        c.fillStyle = g; c.strokeStyle = 'rgba(150,20,70,.35)'; c.lineWidth = 0.8;
        var w = 11 * ring[1];
        c.beginPath(); c.moveTo(0, 0);
        c.bezierCurveTo(w, -len * 0.25, w * 0.9, -len * 0.8, 0, -len);
        c.bezierCurveTo(-w * 0.9, -len * 0.8, -w, -len * 0.25, 0, 0);
        c.fill(); c.stroke();
        c.restore();
      }
      if (ri === 1 && open > 0.55) {
        c.fillStyle = '#f2c230'; c.beginPath(); c.ellipse(0, -14, 8 * open, 3.2 * open, 0, 0, TAU); c.fill();
        c.fillStyle = '#c99a12';
        for (var j = -2; j <= 2; j++) { c.beginPath(); c.arc(j * 2.8 * open, -14, 0.9, 0, TAU); c.fill(); }
      }
    });
    c.restore();
  }
  function pad(c, x, y, r, rot) {
    c.save(); c.translate(x, y); c.scale(1, 0.38); c.rotate(rot);
    c.fillStyle = '#3f7d3a'; c.beginPath(); c.moveTo(0, 0); c.arc(0, 0, r, 0.18, TAU - 0.18); c.closePath(); c.fill();
    c.strokeStyle = 'rgba(200,240,170,.35)'; c.lineWidth = 2; c.beginPath();
    for (var i = 0; i < 9; i++) { var a = 0.4 + i * 0.68; c.moveTo(0, 0); c.lineTo(Math.cos(a) * r * 0.9, Math.sin(a) * r * 0.9); }
    c.stroke(); c.restore();
  }

  function hero() {
    var cv = document.getElementById('pond'); if (!cv) return;
    var S = fit(cv), rand = seeded(1815), flowers = [], pads = [], rings = [], petals = [], count = 0;
    var out = document.getElementById('lotuscount');
    function layout() {
      S = fit(cv); pads = []; flowers = [];
      var n = Math.round(S.w / 70);
      for (var i = 0; i < n; i++) pads.push({ x: rand() * S.w, y: S.h * (0.55 + rand() * 0.42), r: 18 + rand() * 30, rot: rand() * TAU, ph: rand() * TAU });
      for (var k = 0; k < Math.max(4, n / 3); k++) flowers.push({ x: rand() * S.w, y: S.h * (0.62 + rand() * 0.33), s: 0.9 + rand() * 0.8, open: 0.3 + rand() * 0.7, t: 1, ph: rand() * TAU });
      flowers.sort(function (a, b) { return a.y - b.y; });
    }
    layout(); window.addEventListener('resize', function () { layout(); });
    function sky(c, w, h, t) {
      var hr = bkkHour(), day = hr > 6 && hr < 18.3, dusk = (hr >= 17.3 && hr < 19) || (hr >= 5.5 && hr < 7);
      var g = c.createLinearGradient(0, 0, 0, h * 0.55);
      if (dusk) { g.addColorStop(0, '#3a2a5c'); g.addColorStop(1, '#f2a07a'); }
      else if (day) { g.addColorStop(0, '#5aa7c4'); g.addColorStop(1, '#cfe9e8'); }
      else { g.addColorStop(0, '#071820'); g.addColorStop(1, '#1d4652'); }
      c.fillStyle = g; c.fillRect(0, 0, w, h * 0.55);
      // the far bank: sugar palms and a chedi, the flat delta
      c.fillStyle = day ? '#2c5a3a' : '#0d2a2b';
      c.beginPath(); c.moveTo(0, h * 0.5);
      for (var x = 0; x <= w; x += 20) c.lineTo(x, h * 0.5 - 6 - Math.sin(x * 0.03) * 3);
      c.lineTo(w, h * 0.55); c.lineTo(0, h * 0.55); c.fill();
      [0.12, 0.2, 0.71, 0.86].forEach(function (f, i) {
        var px = w * f, ph = h * (0.13 + (i % 2) * 0.04), sway = Math.sin(t * 0.7 + i) * 2;
        c.strokeStyle = c.fillStyle; c.lineWidth = 2.2; c.beginPath(); c.moveTo(px, h * 0.5); c.lineTo(px + sway, h * 0.5 - ph); c.stroke();
        for (var k = 0; k < 9; k++) { var a = Math.PI + k * Math.PI / 8; c.beginPath(); c.moveTo(px + sway, h * 0.5 - ph); c.lineTo(px + sway + Math.cos(a) * 16, h * 0.5 - ph + Math.sin(a) * 9 + 6); c.stroke(); }
      });
      var cx = w * 0.42, by = h * 0.5;
      c.beginPath(); c.moveTo(cx - 16, by); c.lineTo(cx - 9, by - 22); c.quadraticCurveTo(cx, by - 30, cx + 9, by - 22); c.lineTo(cx + 16, by); c.fill();
      c.beginPath(); c.moveTo(cx - 2, by - 28); c.lineTo(cx, by - 62); c.lineTo(cx + 2, by - 28); c.fill();
      if (!day) { c.fillStyle = '#fff7d6'; c.beginPath(); c.arc(w * 0.8, h * 0.12, 14, 0, TAU); c.fill(); }
      var wg = c.createLinearGradient(0, h * 0.5, 0, h);
      wg.addColorStop(0, day ? '#5f9ea4' : '#123a44'); wg.addColorStop(1, day ? '#1f5d63' : '#071d23');
      c.fillStyle = wg; c.fillRect(0, h * 0.53, w, h);
      c.strokeStyle = 'rgba(255,255,255,.12)'; c.lineWidth = 1;
      for (var y = h * 0.56; y < h; y += 14) { c.beginPath(); for (var xx = 0; xx <= w; xx += 12) c.lineTo(xx, y + Math.sin(xx * 0.05 + t + y) * 1.5); c.stroke(); }
    }
    loop(function (dt, t) {
      var c = S.c, w = S.w, h = S.h; c.clearRect(0, 0, w, h);
      sky(c, w, h, t);
      pads.forEach(function (p) { pad(c, p.x + Math.sin(t * 0.3 + p.ph) * 3, p.y, p.r, p.rot); });
      rings = rings.filter(function (r) { r.r += dt * 60; r.a -= dt * 0.7; return r.a > 0; });
      rings.forEach(function (r) { c.strokeStyle = 'rgba(255,255,255,' + r.a + ')'; c.lineWidth = 1.5; c.beginPath(); c.ellipse(r.x, r.y, r.r, r.r * 0.35, 0, 0, TAU); c.stroke(); });
      flowers.forEach(function (f) {
        if (f.t < 1) f.t = Math.min(1, f.t + dt * 0.7);
        var rise = f.t, sway = Math.sin(t * 0.8 + f.ph) * 2.5, stemH = 48 * f.s * rise;
        c.strokeStyle = '#4c7d34'; c.lineWidth = 2.4; c.beginPath(); c.moveTo(f.x, f.y); c.quadraticCurveTo(f.x + sway, f.y - stemH / 2, f.x + sway, f.y - stemH); c.stroke();
        lotus(c, f.x + sway, f.y - stemH, f.s * (0.5 + 0.5 * rise), f.open * Math.max(0, rise * 1.4 - 0.4));
      });
      petals = petals.filter(function (p) { p.y += p.vy * dt; p.x += Math.sin(t * 2 + p.ph) * 0.6; p.r += dt; return p.y < h + 20; });
      petals.forEach(function (p) { c.save(); c.translate(p.x, p.y); c.rotate(p.r); c.fillStyle = '#f39ab8'; c.beginPath(); c.ellipse(0, 0, 5, 9, 0, 0, TAU); c.fill(); c.restore(); });
    }, cv);
    cv.addEventListener('pointerdown', function (e) {
      var p = pt(cv, e), y = Math.max(S.h * 0.58, p.y);
      rings.push({ x: p.x, y: y, r: 4, a: 0.8 });
      flowers.push({ x: p.x, y: y, s: 0.9 + Math.random() * 0.7, open: 0.75 + Math.random() * 0.25, t: RM ? 1 : 0, ph: Math.random() * TAU });
      flowers.sort(function (a, b) { return a.y - b.y; });
      if (flowers.length > 60) flowers.shift();
      for (var i = 0; i < 6; i++) petals.push({ x: p.x + rnd(-30, 30), y: rnd(-40, 0), vy: rnd(30, 70), r: rnd(0, 3), ph: rnd(0, 6) });
      count++;
      if (out) out.textContent = T(count + (count === 1 ? ' lotus' : ' lotuses') + ' offered. In 1815 the Mon of Sam Khok met King Rama II with lotuses, and he named the town for them.',
        'ถวายบัวแล้ว ' + count + ' ดอก พ.ศ. 2358 ชาวมอญสามโคกถวายบัวรับเสด็จรัชกาลที่ 2 จึงทรงตั้งชื่อเมืองตามดอกบัว');
    });
  }

  /* ------------------------------------------------------- Rangsit canals */
  function canals() {
    var cv = document.getElementById('canals'); if (!cv) return;
    var S = fit(cv), N = 14, main = 0, dug = [], cells = [], drops = [], harvested = 0;
    var out = document.getElementById('canalread');
    function reset() { main = 0; dug = []; for (var i = 0; i < N; i++) dug.push(0); cells = []; for (var j = 0; j < N * 2; j++) cells.push(0); drops = []; }
    reset();
    function geo() { var w = S.w, h = S.h, rx = Math.max(40, w * 0.07); return { rx: rx, my: h * 0.5, x0: rx + 26, dx: (w - rx - 40) / N, h: h, w: w }; }
    function read() {
      if (!out) return;
      var n = dug.filter(function (d) { return d >= 1; }).length, g = cells.filter(function (v) { return v > 0.3; }).length;
      out.textContent = main < 1 ? T('Tap to dig Khlong Rangsit from the river', 'แตะเพื่อขุดคลองรังสิตจากแม่น้ำ')
        : T(n + ' of 14 canals · ' + Math.round(100 * g / cells.length) + '% of fields planted' + (harvested ? ' · ' + harvested + ' harvests' : ''),
          'ขุดแล้ว ' + n + ' จาก 14 คลอง · นาที่ปลูกแล้ว ' + Math.round(100 * g / cells.length) + '%' + (harvested ? ' · เกี่ยวแล้ว ' + harvested + ' ครั้ง' : ''));
    }
    read();
    loop(function (dt, t) {
      var c = S.c, G = geo(); c.clearRect(0, 0, G.w, G.h);
      c.fillStyle = '#6f6a4a'; c.fillRect(0, 0, G.w, G.h); // the swamp before the canals
      for (var i = 0; i < N; i++) for (var s = 0; s < 2; s++) {
        var k = i * 2 + s, v = cells[k], wet = main >= 1 && dug[i] >= 1 || (i > 0 && dug[i - 1] >= 1 && main >= 1);
        if (wet && v < 1.6) cells[k] = v + dt * 0.25;
        var x = G.x0 + i * G.dx, y = s ? G.my + 7 : 8, hh = G.my - 15;
        var col = v < 0.3 ? '#6f6a4a' : v < 1.2 ? 'hsl(' + (85 + v * 15) + ',45%,' + (32 + v * 8) + '%)' : 'hsl(' + (95 - (v - 1.2) * 110) + ',60%,48%)';
        c.fillStyle = col; c.fillRect(x - G.dx + 4, y, G.dx - 8, hh);
        if (v > 0.3) {
          c.strokeStyle = 'rgba(255,255,255,.18)'; c.lineWidth = 1;
          for (var yy = y + 6; yy < y + hh; yy += 9) { c.beginPath(); for (var xx = x - G.dx + 8; xx < x - 6; xx += 7) { c.moveTo(xx, yy); c.lineTo(xx + Math.sin(t * 2 + xx * 0.2) * 1.2, yy - 5); } c.stroke(); }
        }
      }
      // Chao Phraya on the west
      c.fillStyle = '#2e8c9a'; c.beginPath(); c.moveTo(0, 0);
      for (var y2 = 0; y2 <= G.h; y2 += 10) c.lineTo(G.rx + Math.sin(y2 * 0.03 + t * 0.6) * 6, y2);
      c.lineTo(0, G.h); c.fill();
      c.save(); c.translate(G.rx * 0.45, G.h * 0.5); c.rotate(-Math.PI / 2); c.fillStyle = '#d6f0f2'; c.font = '600 12px Prompt,sans-serif'; c.textAlign = 'center';
      c.fillText(T('CHAO PHRAYA', 'เจ้าพระยา'), 0, 0); c.restore();
      // main canal
      if (main < 1 && main > 0) main = Math.min(1, main + dt * 0.6);
      var mx = G.rx + (G.w - G.rx) * main;
      c.strokeStyle = '#2e8c9a'; c.lineWidth = 10; c.beginPath(); c.moveTo(G.rx - 4, G.my); c.lineTo(mx, G.my); c.stroke();
      if (main < 1) { c.setLineDash([6, 8]); c.strokeStyle = 'rgba(255,255,255,.5)'; c.lineWidth = 2; c.beginPath(); c.moveTo(mx, G.my); c.lineTo(G.w, G.my); c.stroke(); c.setLineDash([]); }
      for (var j = 0; j < N; j++) {
        var x2 = G.x0 + j * G.dx;
        if (dug[j] > 0 && dug[j] < 1) dug[j] = Math.min(1, dug[j] + dt * 1.4);
        var L = (G.my - 6) * dug[j];
        if (dug[j] > 0) { c.strokeStyle = '#2e8c9a'; c.lineWidth = 5; c.beginPath(); c.moveTo(x2, G.my - L); c.lineTo(x2, G.my + L); c.stroke(); }
        else { c.strokeStyle = 'rgba(255,255,255,.22)'; c.setLineDash([3, 6]); c.lineWidth = 1.5; c.beginPath(); c.moveTo(x2, 6); c.lineTo(x2, G.h - 6); c.stroke(); c.setLineDash([]); }
        c.fillStyle = dug[j] >= 1 ? '#f2c230' : 'rgba(255,255,255,.55)'; c.textAlign = 'center'; c.font = '600 11px Prompt,sans-serif';
        c.fillText(String(j + 1), x2, G.h - 8);
      }
      c.font = '600 12px Prompt,sans-serif'; c.textAlign = 'left';
      var lw = c.measureText(T('Khlong Rangsit', 'คลองรังสิต')).width;
      c.fillStyle = 'rgba(11,42,49,.75)'; c.fillRect(G.rx + 6, G.my - 22, lw + 8, 16);
      c.fillStyle = '#fff'; c.fillText(T('Khlong Rangsit', 'คลองรังสิต'), G.rx + 10, G.my - 9);
      drops = drops.filter(function (d) { d.a -= dt; return d.a > 0; });
      drops.forEach(function (d) { c.fillStyle = 'rgba(214,240,242,' + d.a + ')'; c.beginPath(); c.arc(d.x, d.y - (1 - d.a) * 30, 3, 0, TAU); c.fill(); });
      if (Math.random() < 0.1) read();
    }, cv);
    function dig(p) {
      var G = geo();
      if (main < 1) { if (main === 0) main = 0.001; return; }
      var j = Math.round((p.x - G.x0) / G.dx); j = Math.max(0, Math.min(N - 1, j));
      if (dug[j] === 0) { dug[j] = 0.001; for (var i = 0; i < 8; i++) drops.push({ x: G.x0 + j * G.dx + rnd(-8, 8), y: G.my, a: 1 }); }
    }
    var down = false;
    cv.addEventListener('pointerdown', function (e) { down = true; dig(pt(cv, e)); });
    cv.addEventListener('pointermove', function (e) { if (down && main >= 1) dig(pt(cv, e)); });
    window.addEventListener('pointerup', function () { down = false; });
    window.addEventListener('resize', function () { S = fit(cv); });
    var b1 = document.getElementById('harvest'), b2 = document.getElementById('canalreset');
    if (b1) b1.onclick = function () { var any = false; cells = cells.map(function (v) { if (v > 1.2) { any = true; return 0.31; } return v; }); if (any) harvested++; read(); };
    if (b2) b2.onclick = function () { reset(); harvested = 0; read(); };
  }

  /* ---------------------------------------------------------- Sam Khok jar */
  function jar() {
    var cv = document.getElementById('jar'); if (!cv) return;
    var S = fit(cv), prof = [0.42, 0.62, 0.78, 0.8, 0.68, 0.5, 0.36, 0.4], fired = 0, glow = 0, made = 0, spin = 0, wob = 0;
    var out = document.getElementById('jarread');
    function geo() { var h = S.h, w = S.w; return { cx: w * 0.5, base: h - 52, top: 40, R: Math.min(w * 0.3, 130) }; }
    loop(function (dt, t) {
      var c = S.c, w = S.w, h = S.h, G = geo(); c.clearRect(0, 0, w, h);
      // three kiln mounds behind: sam khok
      for (var m = 0; m < 3; m++) {
        var kx = w * (0.18 + m * 0.32), ky = h - 40;
        c.fillStyle = '#3a2a22'; c.beginPath(); c.ellipse(kx, ky, w * 0.16, h * 0.32, 0, Math.PI, TAU); c.fill();
        c.fillStyle = glow > 0 ? 'rgba(255,' + (120 + 80 * Math.sin(t * 9 + m)) + ',40,' + (0.5 + glow * 0.5) + ')' : '#1a1210';
        c.beginPath(); c.ellipse(kx, ky, 16, 22, 0, Math.PI, TAU); c.fill();
      }
      // wheel
      spin += dt * 6;
      c.fillStyle = '#5b4636'; c.beginPath(); c.ellipse(G.cx, G.base + 8, G.R * 1.15, 14, 0, 0, TAU); c.fill();
      c.strokeStyle = 'rgba(255,255,255,.18)';
      for (var s = 0; s < 6; s++) { var a = spin + s; c.beginPath(); c.moveTo(G.cx, G.base + 8); c.lineTo(G.cx + Math.cos(a) * G.R * 1.1, G.base + 8 + Math.sin(a) * 12); c.stroke(); }
      // jar body from the profile
      var H = G.base - G.top, n = prof.length, wx = Math.sin(t * 12) * wob; wob *= 0.92;
      function r(i) { return prof[i] * G.R; }
      var clay = fired ? 'hsl(' + (18 + glow * 10) + ',' + (55 + glow * 20) + '%,' + (38 + glow * 18) + '%)' : '#a59a8a';
      var g = c.createLinearGradient(G.cx - G.R, 0, G.cx + G.R, 0);
      g.addColorStop(0, 'rgba(0,0,0,.35)'); g.addColorStop(0.45, 'rgba(255,255,255,.12)'); g.addColorStop(1, 'rgba(0,0,0,.4)');
      c.beginPath();
      for (var i = 0; i < n; i++) { var y = G.base - H * i / (n - 1); if (i === 0) c.moveTo(G.cx - r(i) + wx, y); else c.lineTo(G.cx - r(i) + wx, y); }
      for (var k = n - 1; k >= 0; k--) c.lineTo(G.cx + r(k) + wx, G.base - H * k / (n - 1));
      c.closePath(); c.fillStyle = clay; c.fill(); c.fillStyle = g; c.fill();
      // throwing rings and the Mon band
      c.strokeStyle = 'rgba(0,0,0,.18)'; c.lineWidth = 1;
      for (var q = 1; q < 14; q++) { var yq = G.base - H * q / 14, iq = q / 14 * (n - 1), i0 = Math.floor(iq), rr = prof[i0] + (prof[Math.min(n - 1, i0 + 1)] - prof[i0]) * (iq - i0); c.beginPath(); c.ellipse(G.cx + wx, yq, rr * G.R, 3, 0, 0, Math.PI); c.stroke(); }
      c.fillStyle = 'rgba(0,0,0,.25)'; c.beginPath(); c.ellipse(G.cx + wx, G.top, r(n - 1), 6, 0, 0, TAU); c.fill();
      if (fired && glow > 0) glow = Math.max(0, glow - dt * 0.25);
    }, cv);
    function shape(p) {
      if (fired) { wob = 6; return; }
      var G = geo(), H = G.base - G.top, i = Math.round((G.base - p.y) / H * (prof.length - 1));
      if (i < 0 || i >= prof.length) return;
      var v = Math.max(0.18, Math.min(0.98, Math.abs(p.x - G.cx) / G.R));
      prof[i] = v; if (i > 0) prof[i - 1] = (prof[i - 1] * 2 + v) / 3; if (i < prof.length - 1) prof[i + 1] = (prof[i + 1] * 2 + v) / 3;
    }
    var down = false;
    cv.addEventListener('pointerdown', function (e) { down = true; shape(pt(cv, e)); });
    cv.addEventListener('pointermove', function (e) { if (down) shape(pt(cv, e)); });
    window.addEventListener('pointerup', function () { down = false; });
    window.addEventListener('resize', function () { S = fit(cv); });
    var bf = document.getElementById('fire'), bn = document.getElementById('newjar');
    if (bf) bf.onclick = function () { if (fired) { wob = 6; return; } fired = 1; glow = 1; made++; if (out) out.textContent = T(made + ' fired. Sam Khok means three mounds: the kilns on the river bank.', 'เผาแล้ว ' + made + ' ใบ สามโคก คือเนินเตาเผาสามเนินริมแม่น้ำ'); };
    if (bn) bn.onclick = function () { fired = 0; glow = 0; prof = [0.42, 0.62, 0.78, 0.8, 0.68, 0.5, 0.36, 0.4]; };
  }

  /* ------------------------------------------------------ openbill storks */
  function storks() {
    var cv = document.getElementById('storks'); if (!cv) return;
    var S = fit(cv), birds = [], snails = [], eaten = 0, out = document.getElementById('storkread');
    function trees() { var w = S.w, h = S.h; return [[w * 0.18, h * 0.42, 70], [w * 0.5, h * 0.36, 90], [w * 0.82, h * 0.44, 66]]; }
    function perch() {
      birds = []; trees().forEach(function (tr) { for (var i = 0; i < 6; i++) { var a = rnd(-2.6, -0.5), r = tr[2] * rnd(0.4, 0.9); var x = tr[0] + Math.cos(a) * r, y = tr[1] + Math.sin(a) * r * 0.7; birds.push({ x: x, y: y, hx: x, hy: y, st: 'sit', ph: rnd(0, 6), vx: 0, vy: 0, a: 0, tgt: null }); } });
    }
    perch();
    function bird(c, b, t) {
      c.save(); c.translate(b.x, b.y);
      var fly = b.st !== 'sit', flap = fly ? Math.sin(t * 10 + b.ph) : 0, dir = b.vx < 0 ? -1 : 1;
      c.scale(dir, 1);
      c.fillStyle = '#eceae2'; c.beginPath(); c.ellipse(0, 0, 11, 6, 0, 0, TAU); c.fill(); // body
      c.beginPath(); c.arc(9, -6, 3.6, 0, TAU); c.fill();
      c.strokeStyle = '#b9a98a'; c.lineWidth = 1.6; // the open bill: a gap between the mandibles
      c.beginPath(); c.moveTo(11, -6.5); c.quadraticCurveTo(16, -8, 20, -5); c.moveTo(11, -5); c.quadraticCurveTo(15, -3, 20, -5); c.stroke();
      c.fillStyle = '#1b1b1b';
      if (fly) { c.beginPath(); c.moveTo(-4, -2); c.quadraticCurveTo(-2, -16 * flap - 4, 6, -18 * flap - 2); c.lineTo(4, -1); c.fill(); }
      else { c.beginPath(); c.ellipse(-3, -1, 9, 4.5, -0.15, 0, TAU); c.fill(); c.strokeStyle = '#7a6d55'; c.lineWidth = 1.2; c.beginPath(); c.moveTo(-1, 5); c.lineTo(-1, 11); c.moveTo(2, 5); c.lineTo(2, 11); c.stroke(); }
      c.restore();
    }
    loop(function (dt, t) {
      var c = S.c, w = S.w, h = S.h; c.clearRect(0, 0, w, h);
      var g = c.createLinearGradient(0, 0, 0, h); g.addColorStop(0, '#87b9c9'); g.addColorStop(0.7, '#d9e7d4'); g.addColorStop(0.7, '#5d7c3c'); g.addColorStop(1, '#466230');
      c.fillStyle = g; c.fillRect(0, 0, w, h);
      // wat roof behind the trees
      c.fillStyle = '#b4552e'; c.beginPath(); c.moveTo(w * 0.62, h * 0.7); c.lineTo(w * 0.68, h * 0.5); c.lineTo(w * 0.74, h * 0.7); c.fill();
      c.fillStyle = '#f2c230'; c.fillRect(w * 0.679, h * 0.44, 2, h * 0.06);
      trees().forEach(function (tr) {
        c.strokeStyle = '#3b2c1e'; c.lineWidth = 7; c.beginPath(); c.moveTo(tr[0], h * 0.7); c.lineTo(tr[0], tr[1]); c.stroke();
        c.lineWidth = 2.5; for (var k = 0; k < 6; k++) { var a = -2.7 + k * 0.42; c.beginPath(); c.moveTo(tr[0], tr[1] + 10); c.lineTo(tr[0] + Math.cos(a) * tr[2], tr[1] + Math.sin(a) * tr[2] * 0.7); c.stroke(); }
        c.fillStyle = 'rgba(52,94,40,.55)'; c.beginPath(); c.ellipse(tr[0], tr[1] - tr[2] * 0.25, tr[2] * 0.95, tr[2] * 0.45, 0, 0, TAU); c.fill();
      });
      snails.forEach(function (s) { c.fillStyle = s.eaten ? '#d8cbb0' : '#6b4a2a'; c.beginPath(); c.arc(s.x, s.y, 5, 0, TAU); c.fill(); c.strokeStyle = '#2e2012'; c.lineWidth = 1; c.beginPath(); c.arc(s.x, s.y, 2.5, 0, 4); c.stroke(); });
      birds.forEach(function (b) {
        if (b.st === 'up') { // soar on a thermal
          b.a += dt * 1.6; b.x += Math.cos(b.a + b.ph) * 70 * dt + (b.cx - b.x) * 0.3 * dt; b.y -= 28 * dt; b.vx = -Math.sin(b.a + b.ph);
          if (b.y < h * 0.08) b.st = 'home';
        } else if (b.st === 'home' || b.st === 'eat') {
          var tx = b.st === 'eat' && b.tgt ? b.tgt.x : b.hx, ty = b.st === 'eat' && b.tgt ? b.tgt.y - 8 : b.hy;
          var dx = tx - b.x, dy = ty - b.y, d = Math.hypot(dx, dy) || 1, sp = 120;
          b.vx = dx / d; b.x += dx / d * sp * dt; b.y += dy / d * sp * dt;
          if (d < 4) {
            if (b.st === 'eat' && b.tgt) { if (!b.tgt.eaten) { b.tgt.eaten = 1; eaten++; if (out) out.textContent = T(eaten + (eaten === 1 ? ' apple snail' : ' apple snails') + ' eaten. The open bill holds the shell while the tip cuts the snail out.', 'กินหอยเชอรี่แล้ว ' + eaten + ' ตัว ปากที่อ้าช่วยคาบเปลือกหอยไว้ แล้วใช้ปลายปากตัดเนื้อออก'); } b.tgt = null; b.st = 'home'; }
            else { b.st = 'sit'; b.x = b.hx; b.y = b.hy; }
          }
        }
        bird(c, b, t);
      });
      if (snails.length > 30) snails.shift();
    }, cv);
    cv.addEventListener('pointerdown', function (e) {
      var p = pt(cv, e);
      if (p.y > S.h * 0.72) {
        var s = { x: p.x, y: p.y, eaten: 0 }; snails.push(s);
        var best = null, bd = 1e9;
        birds.forEach(function (b) { if (b.st === 'sit' || b.st === 'home') { var d = Math.hypot(b.x - p.x, b.y - p.y); if (d < bd) { bd = d; best = b; } } });
        if (best) { best.st = 'eat'; best.tgt = s; }
      } else {
        birds.forEach(function (b) { if (Math.hypot(b.x - p.x, b.y - p.y) < 160 || Math.random() < 0.3) { b.st = 'up'; b.cx = p.x + rnd(-40, 40); b.a = rnd(0, 6); } });
      }
    });
    window.addEventListener('resize', function () { S = fit(cv); perch(); });
  }

  /* ---------------------------------------------------------- boat noodles */
  function noodles() {
    var cv = document.getElementById('noodles'); if (!cv) return;
    var S = fit(cv), bowls = [], fall = [], steam = [], n = 0, out = document.getElementById('noodleread'), boat = 200;
    loop(function (dt, t) {
      var c = S.c, w = S.w, h = S.h; c.clearRect(0, 0, w, h);
      c.fillStyle = '#16424a'; c.fillRect(0, 0, w, h);
      c.fillStyle = '#2e8c9a'; c.fillRect(0, h * 0.55, w, h * 0.45);
      c.strokeStyle = 'rgba(255,255,255,.15)';
      for (var y = h * 0.6; y < h; y += 12) { c.beginPath(); for (var x = 0; x < w; x += 10) c.lineTo(x, y + Math.sin(x * 0.04 + t * 2 + y) * 2); c.stroke(); }
      // the boat, its cook and the pot
      boat += dt * 30; var bx = (boat % (w * 0.6 + 260)) - 130, by = h * 0.62 + Math.sin(t * 2) * 2;
      c.fillStyle = '#6b3a1e'; c.beginPath(); c.moveTo(bx - 90, by); c.quadraticCurveTo(bx, by + 26, bx + 90, by); c.lineTo(bx + 100, by - 8); c.lineTo(bx - 100, by - 8); c.fill();
      c.fillStyle = '#3a3a3a'; c.fillRect(bx + 20, by - 26, 34, 18); c.fillStyle = '#c0c0c0'; c.fillRect(bx + 18, by - 30, 38, 5);
      c.fillStyle = '#d9306f'; c.beginPath(); c.arc(bx - 30, by - 30, 9, 0, TAU); c.fill(); // the cook
      c.fillStyle = '#f2c230'; c.beginPath(); c.moveTo(bx - 48, by - 36); c.lineTo(bx - 30, by - 52); c.lineTo(bx - 12, by - 36); c.fill(); // ngob hat
      c.fillStyle = '#2b2b2b'; c.fillRect(bx - 38, by - 22, 16, 16);
      c.strokeStyle = '#8a5a30'; c.lineWidth = 3; c.beginPath(); c.moveTo(bx - 70, by - 20); c.lineTo(bx - 110, by + 20 + Math.sin(t * 2) * 6); c.stroke();
      for (var s = 0; s < 3; s++) { c.strokeStyle = 'rgba(255,255,255,.35)'; c.lineWidth = 2; c.beginPath(); c.moveTo(bx + 30 + s * 8, by - 32); c.quadraticCurveTo(bx + 24 + s * 8 + Math.sin(t * 3 + s) * 6, by - 50, bx + 32 + s * 8, by - 66); c.stroke(); }
      // the bank, the table and the stack
      var tx = w * 0.78, ty = h * 0.5;
      c.fillStyle = '#5b4636'; c.beginPath(); c.moveTo(tx - 110, h); c.lineTo(tx - 90, h * 0.55); c.lineTo(w, h * 0.55); c.lineTo(w, h); c.fill();
      c.fillStyle = '#7cae3a'; c.fillRect(tx - 90, h * 0.53, w, 6);
      c.fillStyle = '#7a5434'; c.fillRect(tx - 70, ty, 140, 10); c.fillRect(tx - 60, ty + 10, 8, h * 0.4); c.fillRect(tx + 52, ty + 10, 8, h * 0.4);
      var lean = bowls.length > 18 ? Math.sin(t * 4) * (bowls.length - 18) * 0.004 : 0;
      c.save(); c.translate(tx, ty); c.rotate(lean);
      bowls.forEach(function (b, i) {
        var yy = -i * 7 - 10;
        c.fillStyle = b; c.beginPath(); c.moveTo(-18, yy); c.lineTo(18, yy); c.lineTo(11, yy + 10); c.lineTo(-11, yy + 10); c.fill();
        c.strokeStyle = 'rgba(0,0,0,.25)'; c.lineWidth = 1; c.beginPath(); c.moveTo(-18, yy); c.lineTo(18, yy); c.stroke();
      });
      c.restore();
      fall = fall.filter(function (f) { f.vy += 900 * dt; f.x += f.vx * dt; f.y += f.vy * dt; f.r += f.vr * dt; return f.y < h + 30; });
      fall.forEach(function (f) { c.save(); c.translate(f.x, f.y); c.rotate(f.r); c.fillStyle = f.col; c.beginPath(); c.moveTo(-18, 0); c.lineTo(18, 0); c.lineTo(11, 10); c.lineTo(-11, 10); c.fill(); c.restore(); });
      steam = steam.filter(function (s) { s.y -= 30 * dt; s.a -= dt * 0.8; return s.a > 0; });
      steam.forEach(function (s) { c.strokeStyle = 'rgba(255,255,255,' + s.a + ')'; c.lineWidth = 2; c.beginPath(); c.moveTo(s.x, s.y); c.quadraticCurveTo(s.x + 6, s.y - 8, s.x, s.y - 16); c.stroke(); });
    }, cv);
    var cols = ['#e6e2d6', '#f2c230', '#d9306f', '#2e8c9a', '#7cae3a'];
    cv.addEventListener('pointerdown', function () {
      var w = S.w, h = S.h, tx = w * 0.78, ty = h * 0.5;
      if (bowls.length >= 26) {
        bowls.forEach(function (b, i) { fall.push({ x: tx, y: ty - i * 7 - 10, vx: rnd(-160, 160), vy: rnd(-300, -80), r: 0, vr: rnd(-8, 8), col: b }); });
        bowls = []; if (out) out.textContent = T('The stack fell. ' + n + ' bowls today.', 'กองล้มแล้ว วันนี้ ' + n + ' ชาม'); return;
      }
      bowls.push(cols[n % cols.length]); n++;
      steam.push({ x: tx, y: ty - bowls.length * 7 - 12, a: 1 });
      if (out) out.textContent = T(n + (n === 1 ? ' bowl' : ' bowls') + '. Boat noodles come in small bowls, so people stack them.', n + ' ชาม ก๋วยเตี๋ยวเรือชามเล็ก จึงกินกันทีละหลายชามแล้ววางซ้อน');
    });
    window.addEventListener('resize', function () { S = fit(cv); });
  }

  /* ------------------------------------------------- calendar, numbers, faces, pictures */
  function calendar() {
    var box = document.getElementById('evlist'), data = document.getElementById('evdata'); if (!box || !data) return;
    var rows = JSON.parse(data.textContent), today = new Date(Date.now() + 7 * 3600e3).toISOString().slice(0, 10);
    var lim = new Date(Date.now() + 7 * 3600e3 + 75 * 864e5).toISOString().slice(0, 10);
    var M = TH ? ['ม.ค.', 'ก.พ.', 'มี.ค.', 'เม.ย.', 'พ.ค.', 'มิ.ย.', 'ก.ค.', 'ส.ค.', 'ก.ย.', 'ต.ค.', 'พ.ย.', 'ธ.ค.'] : ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    var shown = rows.filter(function (r) { return (r.end || r.start) >= today && r.start <= lim; });
    if (!shown.length) { box.innerHTML = '<p class="empty">' + T('Nothing dated in the next weeks yet.', 'ยังไม่มีงานที่ระบุวันในช่วงนี้') + '</p>'; return; }
    box.innerHTML = shown.map(function (r) {
      var d = r.start < today ? today : r.start, m = +d.slice(5, 7) - 1, dd = +d.slice(8, 10);
      var span = r.end && r.end !== r.start ? ' – ' + (+r.end.slice(8, 10)) + ' ' + M[+r.end.slice(5, 7) - 1] : '';
      return '<div class="ev ' + (r.kind || '') + '"><div class="d" role="button" tabindex="0">' + dd + '<small>' + M[m] + '</small></div><div><b>' + r.t + '</b><span>' + r.w + span + '</span>' +
        (r.u ? '<a href="' + r.u + '" rel="noopener">' + r.s + '</a>' : '') + '</div></div>';
    }).join('');
    box.addEventListener('click', function (e) { var d = e.target.closest('.d'); if (d && !RM) d.animate([{ transform: 'rotate(0)' }, { transform: 'rotate(-12deg) scale(1.15)' }, { transform: 'rotate(8deg)' }, { transform: 'rotate(0)' }], { duration: 500 }); });
  }
  function bits() {
    document.querySelectorAll('.num').forEach(function (n) { n.addEventListener('click', function () { n.classList.remove('pop'); void n.offsetWidth; n.classList.add('pop'); }); });
    document.querySelectorAll('.face').forEach(function (f) { f.addEventListener('click', function () { if (!RM) f.animate([{ transform: 'rotate(0)' }, { transform: 'rotate(360deg) scale(1.2)' }, { transform: 'rotate(360deg)' }], { duration: 700, easing: 'ease-out' }); }); });
    var lb = document.getElementById('lb');
    if (lb && lb.showModal) document.addEventListener('click', function (e) {
      var im = e.target.closest('img[data-full]'); if (!im) return;
      lb.querySelector('img').src = im.getAttribute('data-full'); lb.querySelector('img').alt = im.alt; lb.querySelector('p').innerHTML = im.getAttribute('data-cap') || ''; lb.showModal();
    });
    if (lb) lb.addEventListener('click', function (e) { if (e.target === lb) lb.close(); });
  }
  function start() { hero(); canals(); jar(); storks(); noodles(); calendar(); bits(); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
})();
