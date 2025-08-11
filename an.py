import os
import re
import sys
import uuid
import json
import time
import random
import requests

class A:
    def __init__(self):
        self.pat_cok = 'cookie.txt'
        self.pat_kom = 'text_komen.txt'

    def cek_file_ada(self):
        for file_name in [self.pat_cok, self.pat_kom]:
            if not os.path.isfile(file_name):
                exit(f'\n[!] File {file_name} tidak ditemukan')

class komentar:
    def __init__(self, cookies_actor):
        self.get_headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en,id;q=0.9,en-GB;q=0.8,en-US;q=0.7',
            'cache-control': 'no-cache',
            'dpr': '1.25',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'referer': 'https://www.facebook.com/',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
            'sec-ch-ua-full-version-list': '"Not)A;Brand";v="8.0.0.0", "Chromium";v="138.0.7204.169", "Microsoft Edge";v="138.0.3351.109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"19.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
            'viewport-width': '744',
        }
        self.pos_headers = {
            'accept': '*/*',
            'accept-language': 'en,id;q=0.9,en-GB;q=0.8,en-US;q=0.7',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.facebook.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.facebook.com/',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
            'sec-ch-ua-full-version-list': '"Not)A;Brand";v="8.0.0.0", "Chromium";v="138.0.7204.169", "Microsoft Edge";v="138.0.3351.109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"19.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
            'x-asbd-id': '359341',
            'x-fb-friendly-name': 'useCometUFICreateCommentMutation',
            'x-fb-lsd': 'fuWurejmQAqt5s5nUFytkY',
        }
        self.cookie = cookies_actor

    def paylod(self, x):
        try:
            self.id_group = re.search(r'"Group","id":"(\d+)"', x).group(1)
            self.feed_back_id = re.search(r'"feedback":{"id":"(.*?)"', x).group(1)
            self.hsi = re.search(r'"hsi":"(\d+)"', x).group(1)
            self.haste_session = re.search(r'"haste_session":"(.*?)"', x).group(1)
            self.actor_id = re.search(r'"actorID":"(\d+)"', x).group(1)
            self.lsd_token = re.search(r'"LSD",\[\],{"token":"(.*?)"', x).group(1)
            self.fb_dtsg = re.search(r'{"name":"fb_dtsg","value":"(.*?)"', x).group(1)
            self.jazoest = re.search(r'"name":"jazoest","value":"(\d+)"', x).group(1)
            self.spint_t = re.search(r'"__spin_t":(\d+)', x).group(1)
            self.rev_sr = re.search(r'"__spin_r":(\d+)', x).group(1)
            self.feed_location = re.search('"feedLocation":"(.*?)"', x).group(1)
            self.feed_source = re.search('"feedbackSource":(.*?),', x).group(1)
            self.router = ''
            self.aatv2 = re.search('"tracePolicy":"(.*?)"', x).group(1)
            self.type = 'img'
        except AttributeError:
            self.id_group = re.search(r'"Group","id":"(\d+)"', x).group(1)
            self.feed_back_id = re.search(r'"feedback":{"id":"(.*?)"', x).group(1)
            self.hsi = re.search(r'"hsi":"(\d+)"', x).group(1)
            self.haste_session = re.search(r'"haste_session":"(.*?)"', x).group(1)
            self.actor_id = re.search(r'"actorID":"(\d+)"', x).group(1)
            self.lsd_token = re.search(r'"LSD",\[\],{"token":"(.*?)"', x).group(1)
            self.fb_dtsg = re.search(r'"dtsg":{"token":"(.*?)"', x).group(1)
            self.jazoest = re.search(r'jazoest=(\d+)', x).group(1)
            self.spint_t = re.search(r'"__spin_t":(\d+)', x).group(1)
            self.rev_sr = re.search(r'"__spin_r":(\d+)', x).group(1)
            self.feed_location = re.search('"feedLocation":"(.*?)"', x).group(1)
            self.feed_source = re.search('"feedbackSource":(.*?),', x).group(1)
            self.router = ''
            self.aatv2 = re.search('"tracePolicy":"(.*?)"', x).group(1)
            self.type = 'text'
        return (self.aatv2, self.router, self.feed_location, self.feed_source, self.type,
                self.id_group, self.feed_back_id, self.hsi, self.haste_session,
                self.actor_id, self.lsd_token, self.fb_dtsg, self.jazoest,
                self.spint_t, self.rev_sr)

    def variabel(self, target_url, text_komen):
        try:
            self.get_headers.update({'cookie': self.cookie})
            self.resp = requests.get(target_url, headers=self.get_headers).text
            self.ganti_url = self.validate_url(target_url, self.resp)
            if self.ganti_url != False:
                self.resp = requests.get(self.ganti_url, headers=self.get_headers).text
            self.aatv2, self.crn, self.feed_location, self.feed_source, self.tipe, \
            self.id_group, self.feed_back_id, self.hsi, self.haste_session, self.actor_id, \
            self.lsd_token, self.fb_dtsg, self.jazoest, self.spint_t, self.rev_sr = self.paylod(self.resp)

            self.data = {
                'av': self.actor_id,
                '__aaid': '0',
                '__user': self.actor_id,
                '__a': '1',
                '__req': '2h',
                '__hs': self.haste_session,
                'dpr': '1',
                '__ccg': 'EXCELLENT',
                '__rev': self.rev_sr,
                '__s': 'gg2w7h:eueg8e:n06277',
                '__hsi': self.hsi,
                '__dyn': '7xeUjGU5a5Q1ryaxG4Vp41twWwIxu13wFwkUKewSwAyUco2qwJyE24wJwpUe8hwaG1sw9u0LVEtwMw6ywMwto886C11wBz83WwgEcEhwGxu782lwv89kbxS1Fwc61awhUC7Udo5qfK0zEkxe2GewGwkUe9obrwh8lwUwgojUlDw-wSU8o4Wm7-2K0-obUG2-azqwaW223908O3216xi4UK2K2WEjxK2B08-269wkopg6C13xecwBwWwjHDzUiBG2OUqwjVqwLwHwa211wo83KwHwOyUqxG',
                '__csr': 'g43M8QaM_4YdMxln4MBf2YQkyq19lRf4Ey9YahRnN2h4Cz8jaQyp3kL6jkF-CgG8AAJh38ICLKZ9PaQIKmGClTCGhqGjiVqmRGKRmhCTinjGG-AFLCKirBih4CO4GurhdAGum8AQOkKAnGiARgBeXDCXyoyVrHQHmKe_CKS9BDoGh6GZ5heXG9GGy9VEhBVooiDxx7zenUC4KEGFFaCV8SiayRwDmq6QehppppVQfyWxN7K2iQ4bKdF1iibXUOfxGcxmq2uEWjQjz9V8nAAKdz8gF2FUjACyoG8ypUbpXyU-6qGUgyayU_xy58K26bK2GUd8lxm9yo98gxu8xy4US2aueK3qrCxKbAUeGx2cDG4VpQmmEeUgy9rzUbovxOfxe9KbwPDxy22qEuwXwGwDwKx21EG3G2K1QzK6UHJ0TJ4ho88S8wau0xodo76t2o6a7C0Q-0CA3fwyxCi1fK7o883RG1EwEwm89lyUfBmiU7_weu581042aQQq5ARyUW79o9pWw2wo0eGo3QXBU6Si6-4U08g9U0pFw7MCwFw8_Cw3B81rQ01NiU0654gElgoHof81bpo6G0_81g40rlw2ScqS0fMwuC0n60yoxo3rxS0ESCfwJgqDz8kwfR028qw2eHDgK18wduq4z01361uw194MS0N80-KA0r902DU1PU4u0dEw1hGGiwnVt03NO1y1OwqoeE6a0mww1vE4mdz8fk0ei86E5OeF01py1OweK0bygy36043Fi0oOwxw2QogwgE28y80MO0fDw',
                '__hblp': '0lA5NjhoGA7e8wh8cEiofUcES2m7ErwyBwwxm4awaS2W588E-0iO5UaUefwTyU3jy988EjwLxu7o8UnyE4h5xWu6FLxOGwVz85mi8xe2O2h0Ywroe8rzobE4q1swHAyE7mU4e685GEowoErxSbG8ACyUnwsUb8oxm3a3G1MAxa1mgvxS2C1nwCjg982rwIwOx2m0yoswid0locU9ovwmu2SmQ4po-2CfwYwu87e3K2S16wj8hwbKt1-2G2m0Wi0io2rxO6o4y6omwc6exO0k-5oaUK5XwlU-4UfU-cx61owsUC2u1Cwxy8kwAwtEG3a0R89U6_wNwqE5-1AwCwt8kwYwmobEK3a1NwMwdO7UW9o8EaQbw-g9Uqx62aQ1ewro5qUgx-2648Obw5Wwg83azo2txC48pwkayU7C3y2yF8c8G1CxycwlUCE9K3K1zg528xC3ifxSU521Nw8m1awRCyWLwRxG2S0z8ao9E2jw5jxW1yAxJ1m1AwTxK1pxi2C0mF0rE5OhQ3ngfFUC6ohzoR1-dxGA3q12BK0xEy18xa0iu2e',
                '__sjsp': 'g4d2aEgAz4aNF36668yA6PgMh8iAD5E8Ex4yj8owSrv92I43mQP7baWegd4N5qPBbIAxnczEIIiGIj8y4Va4eZIVnkwou94cEKqAuOr8b88UxoQAVk4WKj89mtwRIggKq2jYFr-d89yYBkmbAgxDgR3swJHajh1ecmEV29CCjCy9UkBg86A48EMB235xpD8um7UCaUpiBAZ11BKa8t7KmibjhuFUGaGAEggK9p11V4gyQqlnXhtAV4gUpgS8x69BIwSPCqqhCRVbHQlcx8mlmkMTykgEwGA9Rhd8N2tqiZ7g-2idglOO4xyayXg-ha7k9zoCcaERdodkagnyE9py1mp4Du2m4A5Uigemi8Fjh1GgaS722Ehx6544EfFVk1XgO68pCDnwhU2hwFJ0rQ3Bpogxt3Yw8Q290Ug2-g14Q10xO2O3W7U3ewvV40KB71u1fwMxMAhgadw4Yw4mIQE25f402Do3PhbwGwTwOBwe-085GF80Au0Io',
                '__comet_req': '15',
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoest,
                'lsd': self.lsd_token,
                '__spin_r': self.rev_sr,
                '__spin_b': 'trunk',
                '__spin_t': self.spint_t,
                '__crn': 'comet.fbweb.CometSinglePostDialogRoute',
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'useCometUFICreateCommentMutation',
                'variables': json.dumps({
                    "feedLocation": "POST_PERMALINK_DIALOG",
                    "feedbackSource": 2,
                    "groupID": self.id_group,
                    "input": {
                        "client_mutation_id": "2",
                        "actor_id": self.actor_id,
                        "attachments": None,
                        "feedback_id": self.feed_back_id,
                        "formatting_style": None,
                        "message": {"ranges": [], "text": text_komen},
                        "attribution_id_v2": "CometSinglePostDialogRoot.react,comet.post.single_dialog,unexpected,1753757709130,280723,,,;CometGroupDiscussionRoot.react,comet.group,unexpected,1753757690084,760465,2361831622,229#230#301,;SearchCometGlobalSearchDefaultTabRoot.react,comet.search_results.default_tab,unexpected,1753757682549,99864,391724414624676,,;SearchCometGlobalSearchDefaultTabRoot.react,comet.search_results.default_tab,via_cold_start,1753757675760,251060,391724414624676,,",
                        "vod_video_timestamp": None,
                        "is_tracking_encrypted": True,
                        "tracking": [json.dumps({
                            "assistant_caller": "comet_above_composer",
                            "conversation_guide_session_id": str(uuid.uuid4()),
                            "conversation_guide_shown": None
                        })],
                        "feedback_source": "OBJECT",
                        "idempotence_token": f"client:{str(uuid.uuid4())}",
                        "session_id": str(uuid.uuid4()),
                        "downstream_share_session_id": str(uuid.uuid4()),
                        "downstream_share_session_origin_uri": str(target_url),
                        "downstream_share_session_start_time": str(int(time.time()))
                    },
                    "inviteShortLinkKey": None,
                    "renderLocation": None,
                    "scale": 1,
                    "useDefaultActor": False,
                    "focusCommentID": None,
                    "__relay_internal__pv__IsWorkUserrelayprovider": False
                }),
                'server_timestamps': 'true',
                'doc_id': '31298946176359309',
            }
            self.pos_headers.update({'cookie': self.cookie})
            self.msg = requests.post('https://www.facebook.com/api/graphql/', data=self.data, headers=self.pos_headers).text
            if '"errorSummary":"Sesi telah berakhir"' in self.msg or 'session_expired' in self.msg:
                print('Sesi akun ini sudah expired, login ulang')
                return False
            else:
                print('Komentar berhasil dikirim')
                return True
        except Exception as e:
            print(f"Error saat komentar: {e}")
            return False

    def validate_url(self, url, html_text):
        # Contoh sederhana: jika ada redirect share link ke permalink asli
        redirect = re.search(r'href="(https://www.facebook.com/groups/\d+/permalink/\d+/)"', html_text)
        if redirect:
            return redirect.group(1)
        else:
            return False

def update_target():
    url_raw = "https://raw.githubusercontent.com/username/repo/branch/target.txt"
    file_target = 'target.txt'
    try:
        r = requests.get(url_raw, timeout=15)
        if r.status_code == 200:
            with open(file_target, 'w', encoding='utf-8') as f:
                f.write(r.text)
            print("[✓] target.txt berhasil diupdate dari GitHub")
        else:
            print(f"[!] Gagal update target.txt, status code {r.status_code}")
    except Exception as e:
        print(f"[!] Error update target.txt: {e}")

def main():
    print("[*] Mengecek file cookie dan komen...")
    cek = A()
    cek.cek_file_ada()

    print("[*] Mengupdate target.txt dari GitHub...")
    update_target()

    with open('cookie.txt', 'r', encoding='utf-8') as f:
        cookies = f.read().strip()

    with open('text_komen.txt', 'r', encoding='utf-8') as f:
        komentar_list = [line.strip() for line in f if line.strip()]

    with open('target.txt', 'r', encoding='utf-8') as f:
        targets = [line.strip() for line in f if line.strip()]

    bot = komentar(cookies)

    for target_url in targets:
        text_komen = random.choice(komentar_list)
        print(f"[~] Mengomentari: {target_url}")
        success = bot.variabel(target_url, text_komen)
        if not success:
            print("[!] Gagal komentar, cek kembali cookie atau sesi telah expired.")
        time.sleep(5)  # delay antar komentar

if __name__ == '__main__':
    main()
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"19.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
            'viewport-width': '744',
        }
        self.pos_headers = {
            # headers seperti di kode kamu
            'accept': '*/*',
            'accept-language': 'en,id;q=0.9,en-GB;q=0.8,en-US;q=0.7',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.facebook.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.facebook.com/',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
            'sec-ch-ua-full-version-list': '"Not)A;Brand";v="8.0.0.0", "Chromium";v="138.0.7204.169", "Microsoft Edge";v="138.0.3351.109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"19.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
            'x-asbd-id': '359341',
            'x-fb-friendly-name': 'useCometUFICreateCommentMutation',
            'x-fb-lsd': 'fuWurejmQAqt5s5nUFytkY',
        }
        self.cookie = cookies_actor

    def paylod(self, x):
        try:
            self.id_group = re.search(r'"Group","id":"(\d+)"', x).group(1)
            self.feed_back_id = re.search(r'"feedback":{"id":"(.*?)"', x).group(1)
            self.hsi = re.search(r'"hsi":"(\d+)"', x).group(1)
            self.haste_session = re.search(r'"haste_session":"(.*?)"', x).group(1)
            self.actor_id = re.search(r'"actorID":"(\d+)"', x).group(1)
            self.lsd_token = re.search(r'"LSD",\[\],{"token":"(.*?)"', x).group(1)
            self.fb_dtsg = re.search(r'{"name":"fb_dtsg","value":"(.*?)"', x).group(1)
            self.jazoest = re.search(r'"name":"jazoest","value":"(\d+)"', x).group(1)
            self.spint_t = re.search(r'"__spin_t":(\d+)', x).group(1)
            self.rev_sr = re.search(r'"__spin_r":(\d+)', x).group(1)
            self.feed_location = re.search('"feedLocation":"(.*?)"', x).group(1)
            self.feed_source = re.search('"feedbackSource":(.*?),', x).group(1)
            self.router = ''
            self.aatv2 = re.search('"tracePolicy":"(.*?)"', x).group(1)
            self.type = 'img'
        except AttributeError:
            self.id_group = re.search(r'"Group","id":"(\d+)"', x).group(1)
            self.feed_back_id = re.search(r'"feedback":{"id":"(.*?)"', x).group(1)
            self.hsi = re.search(r'"hsi":"(\d+)"', x).group(1)
            self.haste_session = re.search(r'"haste_session":"(.*?)"', x).group(1)
            self.actor_id = re.search(r'"actorID":"(\d+)"', x).group(1)
            self.lsd_token = re.search(r'"LSD",\[\],{"token":"(.*?)"', x).group(1)
            self.fb_dtsg = re.search(r'"dtsg":{"token":"(.*?)"', x).group(1)
            self.jazoest = re.search(r'jazoest=(\d+)', x).group(1)
            self.spint_t = re.search(r'"__spin_t":(\d+)', x).group(1)
            self.rev_sr = re.search(r'"__spin_r":(\d+)', x).group(1)
            self.feed_location = re.search('"feedLocation":"(.*?)"', x).group(1)
            self.feed_source = re.search('"feedbackSource":(.*?),', x).group(1)
            self.router = ''
            self.aatv2 = re.search('"tracePolicy":"(.*?)"', x).group(1)
            self.type = 'text'
        return (self.aatv2, self.router, self.feed_location, self.feed_source, self.type,
                self.id_group, self.feed_back_id, self.hsi, self.haste_session,
                self.actor_id, self.lsd_token, self.fb_dtsg, self.jazoest,
                self.spint_t, self.rev_sr)

    def variabel(self, target_url, text_komen):
        try:
            self.get_headers.update({'cookie': self.cookie})
            self.resp = requests.get(target_url, headers=self.get_headers).text
            self.ganti_url = self.validate_url(target_url, self.resp)
            if self.ganti_url != False:
                self.resp = requests.get(self.ganti_url, headers=self.get_headers).text
            self.attv2, self.crn, self.feed_location, self.feed_source, self.tipe, \
            self.id_group, self.feed_back_id, self.hsi, self.haste_session, self.actor_id, \
            self.lsd_token, self.fb_dtsg, self.jazoest, self.spint_t, self.rev_sr = self.paylod(self.resp)

            self.data = {
                'av': self.actor_id,
                '__aaid': '0',
                '__user': self.actor_id,
                '__a': '1',
                '__req': '2h',
                '__hs': self.haste_session,
                'dpr': '1',
                '__ccg': 'EXCELLENT',
                '__rev': self.rev_sr,
                '__s': 'gg2w7h:eueg8e:n06277',
                '__hsi': self.hsi,
                '__dyn': '7xeUjGU5a5Q1ryaxG4Vp41twWwIxu13wFwkUKewSwAyUco2qwJyE24wJwpUe8hwaG1sw9u0LVEtwMw6ywMwto886C11wBz83WwgEcEhwGxu782lwv89kbxS1Fwc61awhUC7Udo5qfK0zEkxe2GewGwkUe9obrwh8lwUwgojUlDw-wSU8o4Wm7-2K0-obUG2-azqwaW223908O3216xi4UK2K2WEjxK2B08-269wkopg6C13xecwBwWwjHDzUiBG2OUqwjVqwLwHwa211wo83KwHwOyUqxG',
                '__csr': 'g43M8QaM_4YdMxln4MBf2YQkyq19lRf4Ey9YahRnN2h4Cz8jaQyp3kL6jkF-CgG8AAJh38ICLKZ9PaQIKmGClTCGhqGjiVqmRGKRmhCTinjGG-AFLCKirBih4CO4GurhdAGum8AQOkKAnGiARgBeXDCXyoyVrHQHmKe_CKS9BDoGh6GZ5heXG9GGy9VEhBVooiDxx7zenUC4KEGFFaCV8SiayRwDmq6QehppppVQfyWxN7K2iQ4bKdF1iibXUOfxGcxmq2uEWjQjz9V8nAAKdz8gF2FUjACyoG8ypUbpXyU-6qGUgyayU_xy58K26bK2GUd8lxm9yo98gxu8xy4US2aueK3qrCxKbAUeGx2cDG4VpQmmEeUgy9rzUbovxOfxe9KbwPDxy22qEuwXwGwDwKx21EG3G2K1QzK6UHJ0TJ4ho88S8wau0xodo76t2o6a7C0Q-0CA3fwyxCi1fK7o883RG1EwEwm89lyUfBmiU7_weu581042aQQq5ARyUW79o9pWw2wo0eGo3QXBU6Si6-4U08g9U0pFw7MCwFw8_Cw3B81rQ01NiU0654gElgoHof81bpo6G0_81g40rlw2ScqS0fMwuC0n60yoxo3rxS0ESCfwJgqDz8kwfR028qw2eHDgK18wduq4z01361uw194MS0N80-KA0r902DU1PU4u0dEw1hGGiwnVt03NO1y1OwqoeE6a0mww1vE4mdz8fk0ei86E5OeF01py1OweK0bygy36043Fi0oOwxw2QogwgE28y80MO0fDw',
                '__hblp': '0lA5NjhoGA7e8wh8cEiofUcES2m7ErwyBwwxm4awaS2W588E-0iO5UaUefwTyU3jy988EjwLxu7o8UnyE4h5xWu6FLxOGwVz85mi8xe2O2h0Ywroe8rzobE4q1swHAyE7mU4e685GEowoErxSbG8ACyUnwsUb8oxm3a3G1MAxa1mgvxS2C1nwCjg982rwIwOx2m0yoswid0locU9ovwmu2SmQ4po-2CfwYwu87e3K2S16wj8hwbKt1-2G2m0Wi0io2rxO6o4y6omwc6exO0k-5oaUK5XwlU-4UfU-cx61owsUC2u1Cwxy8kwAwtEG3a0R89U6_wNwqE5-1AwCwt8kwYwmobEK3a1NwMwdO7UW9o8EaQbw-g9Uqx62aQ1ewro5qUgx-2648Obw5Wwg83azo2txC48pwkayU7C3y2yF8c8G1CxycwlUCE9K3K1zg528xC3ifxSU521Nw8m1awRCyWLwRxG2S0z8ao9E2jw5jxW1yAxJ1m1AwTxK1pxi2C0mF0rE5OhQ3ngfFUC6ohzoR1-dxGA3q12BK0xEy18xa0iu2e',
                '__sjsp': 'g4d2aEgAz4aNF36668yA6PgMh8iAD5E8Ex4yj8owSrv92I43mQP7baWegd4N5qPBbIAxnczEIIiGIj8y4Va4eZIVnkwou94cEKqAuOr8b88UxoQAVk4WKj89mtwRIggKq2jYFr-d89yYBkmbAgxDgR3swJHajh1ecmEV29CCjCy9UkBg86A48EMB235xpD8um7UCaUpiBAZ11BKa8t7KmibjhuFUGaGAEggK9p11V4gyQqlnXhtAV4gUpgS8x69BIwSPCqqhCRVbHQlcx8mlmkMTykgEwGA9Rhd8N2tqiZ7g-2idglOO4xyayXg-ha7k9zoCcaERdodkagnyE9py1mp4Du2m4A5Uigemi8Fjh1GgaS722Ehx6544EfFVk1XgO68pCDnwhU2hwFJ0rQ3Bpogxt3Yw8Q290Ug2-g14Q10xO2O3W7U3ewvV40KB71u1fwMxMAhgadw4Yw4mIQE25f402Do3PhbwGwTwOBwe-085GF80Au0Io',
                '__comet_req': '15',
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoest,
                'lsd': self.lsd_token,
                '__spin_r': self.rev_sr,
                '__spin_b': 'trunk',
                '__spin_t': self.spint_t,
                '__crn': 'comet.fbweb.CometSinglePostDialogRoute',
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'useCometUFICreateCommentMutation',
                'variables': json.dumps({
                    "feedLocation": "POST_PERMALINK_DIALOG",
                    "feedbackSource": 2,
                    "groupID": self.id_group,
                    "input": {
                        "client_mutation_id": "2",
                        "actor_id": self.actor_id,
                        "attachments": None,
                        "feedback_id": self.feed_back_id,
                        "formatting_style": None,
                        "message": {"ranges": [], "text": text_komen},
                        "attribution_id_v2": "CometSinglePostDialogRoot.react,comet.post.single_dialog,unexpected,1753757709130,280723,,,;CometGroupDiscussionRoot.react,comet.group,unexpected,1753757690084,760465,2361831622,229#230#301,;SearchCometGlobalSearchDefaultTabRoot.react,comet.search_results.default_tab,unexpected,1753757682549,99864,391724414624676,,;SearchCometGlobalSearchDefaultTabRoot.react,comet.search_results.default_tab,via_cold_start,1753757675760,251060,391724414624676,,",
                        "vod_video_timestamp": None,
                        "is_tracking_encrypted": True,
                        "tracking": [json.dumps({
                            "assistant_caller": "comet_above_composer",
                            "conversation_guide_session_id": str(uuid.uuid4()),
                            "conversation_guide_shown": None
                        })],
                        "feedback_source": "OBJECT",
                        "idempotence_token": f"client:{str(uuid.uuid4())}",
                        "session_id": str(uuid.uuid4()),
                        "downstream_share_session_id": str(uuid.uuid4()),
                        "downstream_share_session_origin_uri": str(target_url),
                        "downstream_share_session_start_time": str(int(time.time()))
                    },
                    "inviteShortLinkKey": None,
                    "renderLocation": None,
                    "scale": 1,
                    "useDefaultActor": False,
                    "focusCommentID": None,
                    "__relay_internal__pv__IsWorkUserrelayprovider": False
                }),
                'server_timestamps': 'true',
                'doc_id': '31298946176359309',
            }
            self.pos_headers.update({'cookie': self.cookie})
            self.msg = requests.post('https://www.facebook.com/api/graphql/', data=self.data, headers=self.pos_headers).text
            self.id_komen = re.findall('"url":"(.*?)"', self.msg)
            for self.y in self.id_komen:
                if 'comment_id' in self.y:
                    print(f'✅ Komentar sukses kirim ke {target_url} : {text_komen}')
                    return True
            print(f'❌ Gagal komentar ke {target_url} : {text_komen}')
            return False
        except Exception as e:
            print(f'❌ Error saat komentar: {e}')
            return False

    def validate_url(self, url, resp_text):
        # Cek redirect ke share atau validasi
        if "www.facebook.com/sharer/sharer.php" in resp_text or "validasi" in resp_text.lower():
            return False
        # Bisa tambah cek lain sesuai kebutuhan
        return False

    def delai(self):
        time.sleep(random.randint(3,6))


def get_targets_from_github_raw(url):
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp.text.strip().splitlines()
        else:
            print(f"[!] Gagal ambil target dari GitHub, status code: {resp.status_code}")
            return []
    except Exception as e:
        print(f"[!] Error ambil target dari GitHub: {e}")
        return []

def Start():
    url_target_github_raw = "https://raw.githubusercontent.com/songsola/Ko/refs/heads/main/poko.txt"  # Ganti sesuai file target kamu

    targets = get_targets_from_github_raw(url_target_github_raw)
    if not targets:
        print("❌ Gagal ambil target dari GitHub, hentikan program.")
        return

    cookies = open('cookie.txt', 'r').read().splitlines()
    komens = open('text_komen.txt', 'r').read().splitlines()

    for target in targets:
        target = target.strip()
        if not ("/groups/" in target and "/permalink/" in target):
            print(f"❌ Link target tidak valid: {target}")
            continue

        for cokie in cookies:
            text_komen = random.choice(komens)
            bot = komentar(cokie)
            bot.variabel(target, text_komen)
            bot.delai()

if __name__=="__main__":
    cek_file.cek_file_ada()
    Start()
                '__hs': self.haste_session,
                'dpr': '1',
                '__ccg': 'EXCELLENT',
                '__rev': self.rev_sr,
                '__s': 'gg2w7h:eueg8e:n06277',
                '__hsi': self.hsi,
                '__dyn': '7xeUjGU5a5Q1ryaxG4Vp41twWwIxu13wFwkUKewSwAyUco2qwJyE24wJwpUe8hwaG1sw9u0LVEtwMw6ywMwto886C11wBz83WwgEcEhwGxu782lwv89kbxS1Fwc61awhUC7Udo5qfK0zEkxe2GewGwkUe9obrwh8lwUwgojUlDw-wSU8o4Wm7-2K0-obUG2-azqwaW223908O3216xi4UK2K2WEjxK2B08-269wkopg6C13xecwBwWwjHDzUiBG2OUqwjVqwLwHwa211wo83KwHwOyUqxG',
                '__csr': 'g43M8QaM_4YdMxln4MBf2YQkyq19lRf4Ey9YahRnN2h4Cz8jaQyp3kL6jkF-CgG8AAJh38ICLKZ9PaQIKmGClTCGhqGjiVqmRGKRmhCTinjGG-AFLCKirBih4CO4GurhdAGum8AQOkKAnGiARgBeXDCXyoyVrHQHmKe_CKS9BDoGh6GZ5heXG9GGy9VEhBVooiDxx7zenUC4KEGFFaCV8SiayRwDmq6QehppppVQfyWxN7K2iQ4bKdF1iibXUOfxGcxmq2uEWjQjz9V8nAAKdz8gF2FUjACyoG8ypUbpXyU-6qGUgyayU_xy58K26bK2GUd8lxm9yo98gxu8xy4US2aueK3qrCxKbAUeGx2cDG4VpQmmEeUgy9rzUbovxOfxe9KbwPDxy22qEuwXwGwDwKx21EG3G2K1QzK6UHJ0TJ4ho88S8wau0xodo76t2o6a7C0Q-0CA3fwyxCi1fK7o883RG1EwEwm89lyUfBmiU7_weu581042aQQq5ARyUW79o9pWw2wo0eGo3QXBU6Si6-4U08g9U0pFw7MCwFw8_Cw3B81rQ01NiU0654gElgoHof81bpo6G0_81g40rlw2ScqS0fMwuC0n60yoxo3rxS0ESCfwJgqDz8kwfR028qw2eHDgK18wduq4z01361uw194MS0N80-KA0r902DU1PU4u0dEw1hGGiwnVt03NO1y1OwqoeE6a0mww1vE4mdz8fk0ei86E5OeF01py1OweK0bygy36043Fi0oOwxw2QogwgE28y80MO0fDw',
                '__hblp': '0lA5NjhoGA7e8wh8cEiofUcES2m7ErwyBwwxm4awaS2W588E-0iO5UaUefwTyU3jy988EjwLxu7o8UnyE4h5xWu6FLxOGwVz85mi8xe2O2h0Ywroe8rzobE4q1swHAyE7mU4e685GEowoErxSbG8ACyUnwsUb8oxm3a3G1MAxa1mgvxS2C1nwCjg982rwIwOx2m0yoswid0locU9ovwmu2SmQ4po-2CfwYwu87e3K2S16wj8hwbKt1-2G2m0Wi0io2rxO6o4y6omwc6exO0k-5oaUK5XwlU-4UfU-cx61owsUC2u1Cwxy8kwAwtEG3a0R89U6_wNwqE5-1AwCwt8kwYwmobEK3a1NwMwdO7UW9o8EaQbw-g9Uqx62aQ1ewro5qUgx-2648Obw5Wwg83azo2txC48pwkayU7C3y2yF8c8G1CxycwlUCE9K3K1zg528xC3ifxSU521Nw8m1awRCyWLwRxG2S0z8ao9E2jw5jxW1yAxJ1m1AwTxK1pxi2C0mF0rE5OhQ3ngfFUC6ohzoR1-dxGA3q12BK0xEy18xa0iu2e',
                '__sjsp': 'g4d2aEgAz4aNF36668yA6PgMh8iAD5E8Ex4yj8owSrv92I43mQP7baWegd4N5qPBbIAxnczEIIiGIj8y4Va4eZIVnkwou94cEKqAuOr8b88UxoQAVk4WKj89mtwRIggKq2jYFr-d89yYBkmbAgxDgR3swJHajh1ecmEV29CCjCy9UkBg86A48EMB235xpD8um7UCaUpiBAZ11BKa8t7KmibjhuFUGaGAEggK9p11V4gyQqlnXhtAV4gUpgS8x69BIwSPCqqhCRVbHQlcx8mlmkMTykgEwGA9Rhd8N2tqiZ7g-2idglOO4xyayXg-ha7k9zoCcaERdodkagnyE9py1mp4Du2m4A5Uigemi8Fjh1GgaS722Ehx6544EfFVk1XgO68pCDnwhU2hwFJ0rQ3Bpogxt3Yw8Q290Ug2-g14Q10xO2O3W7U3ewvV40KB71u1fwMxMAhgadw4Yw4mIQE25f402Do3PhbwGwTwOBwe-085GF80Au0Io',
                '__comet_req': '15',
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoest,
                'lsd': self.lsd_token,
                '__spin_r': self.rev_sr,
                '__spin_b': 'trunk',
                '__spin_t': self.spint_t,
                '__crn': 'comet.fbweb.CometSinglePostDialogRoute',
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'useCometUFICreateCommentMutation',
                'variables': json.dumps({
                    "feedLocation": "POST_PERMALINK_DIALOG",
                    "feedbackSource": 2,
                    "groupID": self.id_group,
                    "input": {
                        "client_mutation_id": "2",
                        "actor_id": self.actor_id,
                        "attachments": None,
                        "feedback_id": self.feed_back_id,
                        "formatting_style": None,
                        "message": {"ranges": [], "text": text_komen},
                        "attribution_id_v2": "CometSinglePostDialogRoot.react,comet.post.single_dialog,unexpected,1753757709130,280723,,,;CometGroupDiscussionRoot.react,comet.group,unexpected,1753757690084,760465,2361831622,229#230#301,;SearchCometGlobalSearchDefaultTabRoot.react,comet.search_results.default_tab,unexpected,1753757682549,99864,391724414624676,,;SearchCometGlobalSearchDefaultTabRoot.react,comet.search_results.default_tab,via_cold_start,1753757675760,251060,391724414624676,,",
                        "vod_video_timestamp": None,
                        "is_tracking_encrypted": True,
                        "tracking": [json.dumps({
                            "assistant_caller": "comet_above_composer",
                            "conversation_guide_session_id": str(uuid.uuid4()),
                            "conversation_guide_shown": None
                        })],
                        "feedback_source": "OBJECT",
                        "idempotence_token": f"client:{str(uuid.uuid4())}",
                        "session_id": str(uuid.uuid4()),
                        "downstream_share_session_id": str(uuid.uuid4()),
                        "downstream_share_session_origin_uri": str(target_url),
                        "downstream_share_session_start_time": str(int(time.time()))
                    },
                    "inviteShortLinkKey": None,
                    "renderLocation": None,
                    "scale": 1,
                    "useDefaultActor": False,
                    "focusCommentID": None,
                    "__relay_internal__pv__IsWorkUserrelayprovider": False
                }),
                'server_timestamps': 'true',
                'doc_id': '31298946176359309',
            }
            self.pos_headers.update({'cookie': self.cookie})
            self.msg = requests.post('https://www.facebook.com/api/graphql/', data=self.data, headers=self.pos_headers).text
            self.id_komen = re.findall('"url":"(.*?)"', self.msg)
            for y in self.id_komen:
                if 'comment_id' in y:
                    print(f'✅ Komentar sukses kirim ke {target_url} : {text_komen}')
                    return True
            print(f'❌ Gagal komentar ke {target_url} : {text_komen}')
            return False
        except Exception as e:
            print(f'❌ Error saat komentar: {e}')
            return False

    def validate_url(self, url, resp_text):
        # Cek redirect ke share atau validasi
        if "www.facebook.com/sharer/sharer.php" in resp_text or "validasi" in resp_text.lower():
            return False
        return False

    def delai(self):
        delay = random.randint(3, 6)
        print(f"[*] Delay {delay} detik...")
        time.sleep(delay)

def update_target_only(repo_folder='.'):
    try:
        print("[*] Mengambil update terbaru dari GitHub (fetch)...")
        fetch = subprocess.run(['git', '-C', repo_folder, 'fetch'], capture_output=True, text=True, timeout=30)
        if fetch.returncode != 0:
            print(f"[!] Git fetch error: {fetch.stderr}")
            return False

        print("[*] Mengupdate file target.txt saja dari remote origin/main...")
        checkout = subprocess.run(['git', '-C', repo_folder, 'checkout', 'origin/main', '--', 'target.txt'],
                                  capture_output=True, text=True, timeout=30)
        if checkout.returncode == 0:
            print("[✓] target.txt berhasil diupdate dari remote")
            return True
        else:
            print(f"[!] Git checkout error: {checkout.stderr}")
            return False
    except Exception as e:
        print(f"[!] Exception saat update target.txt: {e}")
        return False

def main():
    bot = A()
    bot.cek_file_ada()

    # Update target.txt dulu
    update_target_only()

    cookies = []
    with open(bot.pat_cok, 'r') as f:
        cookies = [x.strip() for x in f if x.strip()]

    komentar_text = []
    with open(bot.pat_kom, 'r') as f:
        komentar_text = [x.strip() for x in f if x.strip()]

    # Baca target dari file target.txt (satu URL per baris)
    if not os.path.isfile('target.txt'):
        exit("[!] target.txt tidak ditemukan")

    with open('target.txt', 'r') as f:
        targets = [x.strip() for x in f if x.strip()]

    print(f"[*] Mulai komentar ke {len(targets)} target dengan {len(cookies)} akun dan {len(komentar_text)} komentar")

    for cookie in cookies:
        k = komentar(cookie)
        for target_url in targets:
            komen = random.choice(komentar_text)
            sukses = k.variabel(target_url, komen)
            k.delai()
            if not sukses:
                print("[!] Ada error atau komentar gagal, lanjutkan akun/target berikutnya...")

if __name__ == '__main__':
    main()
