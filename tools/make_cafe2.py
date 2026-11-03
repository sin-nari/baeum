# cafe30.html(30분 운영 원본) → cafe.html · cafe2.html(20분 운영, 11. 3. 실제 운영)
# cafe30.html을 고친 뒤:  python3 tools/make_cafe2.py
import pathlib, sys
root = pathlib.Path(__file__).resolve().parent.parent
s = (root/"cafe30.html").read_text(encoding="utf-8")
R = [
 ('<title>고등학교 교육과정 이야기 카페 · 배움:성장</title>', '<title>이야기 카페 (20분 운영) · 배움:성장</title>'),
 ('<div class="kick">부천 배움 100이음 · 「배움:성장」 사례 공유형 직무연수</div>',
  '<div class="kick">부천 배움 100이음 · 「배움:성장」 사례 공유형 직무연수 · <b style="background:#ffe28a;color:#1d3a40;padding:2px 10px;border-radius:999px">20분 운영</b></div>'),
 ('15:30~17:30 · 등록 15:00', '15:30~17:05 · 등록 15:00'),
 ('<small id="mT1">16:00~16:30</small>', '<small id="mT1">16:00~16:20</small>'),
 ('<small id="mT2">16:35~17:05</small>', '<small id="mT2">16:25~16:45</small>'),
 ('<h2>교시 타이머 · 30분 / 25분</h2>', '<h2>교시 타이머 · 20분</h2>'),
 ('화면 가득 30분(또는 25분)이 흐르고, <b>끝나기 7분 전</b>부터는', '화면 가득 20분이 흐릅니다. <b>사례 이야기 15분 → 질문·토의 3분</b>, <b>마지막 2분</b>은'),
 ('<span>운영 시간</span><label><input type="radio" name="cklen" value="30" checked> 30분</label><label><input type="radio" name="cklen" value="25"> 25분</label>',
  '<span>운영 시간</span><label><input type="radio" name="cklen" value="20" checked> 20분 (사례 15 · 질문·토의 3 · 한 줄 2)</label>'),
 ('16:00~16:30 · 16:23부터 이야기 벽', '16:00~16:20 · 16:18부터 이야기 벽'),
 ('16:35~17:05 · 16:58부터 이야기 벽', '16:25~16:45 · 16:43부터 이야기 벽'),
 ('<b>17:05 행운 추첨</b>', '<b>16:55 행운 추첨</b>'),
 ('<b>17:05 전체 나눔</b>', '<b>16:45 전체 나눔</b>'),
 ('SHARE TIME · 17:05', 'SHARE TIME · 16:45'),
 ('LUCKY DRAW · 17:05', 'LUCKY DRAW · 16:55'),
 ('16:30부터 미리 남길 수 있어요.', '16:20부터 미리 남길 수 있어요.'),
 ('kst("16:30"), kst("23:59"), "11. 3. 16:30에 열려요"', 'kst("16:20"), kst("23:59"), "11. 3. 16:20에 열려요"'),
 ('{ at:"16:00", to:"16:30", nm:"이야기 카페 1교시", ds:"학교별 사례 공유와 질의·토의", p:2 },',
  '{ at:"16:00", to:"16:20", nm:"이야기 카페 1교시", ds:"사례 15분 · 질문·토의 3분 · 한 줄 2분", p:2 },'),
 ('{ at:"16:35", to:"17:05", nm:"이야기 카페 2교시", ds:"1교시와 다른 카페로", p:2 },',
  '{ at:"16:25", to:"16:45", nm:"이야기 카페 2교시", ds:"1교시와 다른 카페로", p:2 },'),
 ('{ at:"17:05", to:"17:30", nm:"전체 나눔", ds:"카페지기 발표 · 분임별 3분 이내", p:2 },',
  '{ at:"16:45", to:"16:55", nm:"전체 나눔", ds:"카페지기 세 분 · 3분씩", p:2 },'),
 ('{ at:"17:30", to:"18:00", nm:"마무리", ds:"만족도 조사와 인사" }',
  '{ at:"16:55", to:"17:05", nm:"행운 추첨 · 마무리", ds:"만족도 조사와 인사" }'),
 ('now < kst("17:30")', 'now < kst("17:05")'),
 ('kst("16:33")', 'kst("16:23")'),
 ('행운 코드(W-…)로 17:05 추첨에도', '행운 코드(W-…)로 16:55 추첨에도'),
 ('src="menu/qr-wall.png"', 'src="menu/qr-wall2.png"'),
 ('2:{s:"16:35", next:', '2:{s:"16:25", next:'),
 ('{ let v = 30; try{ v = +(localStorage.getItem("cafe.cklen") || 30); }catch(e){} if (v !== 25) v = 30; const r = document.querySelector(`input[name=cklen][value="${v}"]`); if (r) r.checked = true; setLen(v); }',
  'setLen(20); try{ localStorage.setItem("cafe.cklen", "30"); }catch(e){}'),
]
for a, b in R:
    n = s.count(a)
    if n < 1: sys.exit(f"못 찾음: {a[:60]}")
    s = s.replace(a, b)
for out in ("cafe.html", "cafe2.html"):
    (root/out).write_text(s, encoding="utf-8")
print("cafe.html · cafe2.html(20분) 만듦,", len(R), "곳 바꿈")
