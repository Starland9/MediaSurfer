import requests
import user_agent
from bs4 import BeautifulSoup
import base64
import random
import time


class InsTaGrAM_ServIcE:
    def Insta_DoWnlOaDeD(self, Url=None):
        s = requests.session()
        s.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
                         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', })

        def session():
            try:
                r = s.get('https://indown.io/reels')
                so = BeautifulSoup(r.text, 'html.parser')
                if r.status_code == 200:
                    t = so.find('input', {'name': '_token'})['value']
                    return t
                else:
                    return False
            except:
                return False
        tk = session()
        if not tk:
            return False
        d = {'referer': 'https://indown.io/reels',
             'locale': 'en', '_token': tk, 'link': Url, 'p': 'i', }
        try:
            r = s.post('https://indown.io/download',
                       data=d, allow_redirects=True)
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, 'html.parser')
                link = soup.find(
                    'video', class_='img-fluid').find('source')['src']
                return link
            else:
                return False
        except:
            return False


class Yt_ServIcE:
    def Yt_DoWnlOaDeD(self, quality=None, type=None, url=None):
        s_yt = requests.session()
        s_yt.headers.update(
            {'User-Agent': user_agent.generate_user_agent(), 'Accept': '*/*'})
        x = s_yt.get('https://ytdown.to/en2/')
        if x.status_code != 200:
            return False
        data = {'url': url}
        response = s_yt.post('https://ytdown.to/proxy.php', data=data)
        if response.status_code == 200 and 'Media unavailable' in response.text:
            return {'status': 'failed', 'reason': 'The Link Unavailable'}
        elif 'Too many requests' in response.text:
            return {'status': 'failed', 'reason': 'Too Many Requests'}
        if response.status_code == 200 and 'api' in response.text:
            d = response.json().get('api').get('mediaItems')
            is_video, is_audio = False, False
            if type and type.capitalize() == 'Video':
                is_video = True
            elif type and type.capitalize() == 'Audio':
                is_audio = True
            for l in d:

                response = requests.get(l.get('mediaUrl')
                                        )
                json_data = response.json()
                final_media_url = json_data.get(
                    'fileUrl') if 'fileUrl' in json_data else json_data.get('url')

                l['mediaUrl'] = final_media_url

                if l.get('type') == 'Video' and is_video:
                    if not quality:
                        return {'status': 'failed', 'reason': 'Please Choice quality'}
                    if quality.lower() not in ['1080p', '480p', '360p', '720p', '240p']:
                        return {'status': 'Failed', 'reason': 'Choice A Current Quality Of Video'}
                    if quality.lower() in l.get('mediaUrl', ''):
                        return {'status': 'success', 'Video_Url': l.get('mediaUrl'), 'quality': quality}
                    continue
                elif l.get('type') == 'Audio' and is_audio:
                    if l.get('mediaUrl'):
                        return {'status': 'success', 'Audio_Url': l.get('mediaUrl')}
                    continue
        else:
            return {'status': 'failed', 'reason': 'Please Provide Url Or Contact @arifi_ios For Fix Issue'}


class TiKToK_ServIcE:
    def TiKToK_DoWnlOaDeD(self, URL):
        s = requests.session()
        s.headers.update({'User-Agent': user_agent.generate_user_agent(),
                         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'})

        def E(URL):
            def gen_ips(): return random.randint(10, 199)
            params = {'url': 'dl'}
            data = {'id': URL, 'locale': 'en', 'tt': 'cEd5alY4',
                    'debug': f'ab=0&loc=USA&ip={gen_ips()}.{gen_ips()}.{gen_ips()}.{gen_ips()}'}
            response = s.post('https://ssstik.io/abc',
                              params=params, data=data)
            if response.status_code == 200:
                try:
                    so = BeautifulSoup(response.text, 'html.parser')
                    url = so.find('a', id='hd_download').get('data-directurl')
                    if not url:
                        return False
                    return url
                except:
                    return False
            else:
                return False
        p2_url = E(URL)
        if not p2_url:
            return False
        data = {'tt': p2_url.split('=')[1]}
        response = s.post(f'https://ssstik.io{p2_url}', data=data)
        if response.status_code == 200 and 'Hx-Redirect' in response.headers:
            l = response.headers['Hx-Redirect'].removeprefix(
                'https://tikcdn.io/ssstik/')
            decoded_url = base64.b64decode(l).decode()
            return decoded_url
        else:
            return False


class SpOtIfY_ServIcE:
    def SpOtIFy_DoWnlOaDeD(self, URL):
        s = requests.session()
        s.headers.update({'User-Agent': user_agent.generate_user_agent(),
                         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'})

        def C():
            response = s.get('https://spotmate.online/en1')
            if response.status_code == 200:
                try:
                    so = BeautifulSoup(response.text, 'html.parser')
                    s.headers.update(
                        {'X-Csrf-Token': so.find('meta', {'name': 'csrf-token'})['content']})
                    return True
                except:
                    return False
            else:
                return False
        x = C()
        if not x:
            return False
        json_data = {'urls': URL}
        try:
            response = s.post(
                'https://spotmate.online/convert', json=json_data)
            if response.status_code == 200 and 'url' in response.text:
                return response.json().get('url').replace('\\', '')
            else:
                return False
        except:
            return False


class FaCeBoOk_ServIcE:
    def FaCeBoOk_DoWnlOaDeD(self, URL):
        import cloudscraper
        s = cloudscraper.create_scraper()
        data = {'URLz': URL}
        try:
            response = s.post('https://fdown.net/download.php', data=data)
            if response.status_code == 200:
                so = BeautifulSoup(response.text, 'html.parser')
                url = so.find('a', class_='btn btn-primary btn-sm')['href']
                return url
            else:
                return False
        except:
            return False


class PiNteResT_ServIcE:
    def PiNteResT_DoWnlOaDeD(self, URL):
        s = requests.session()
        s.headers.update(
            {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'})

        def C():
            params = {'t': int(time.time())}
            try:
                response = requests.get(
                    'https://klickpin.com/get-csrf-token.php', params=params)
                if response.status_code == 200 and 'csrf_token' in response.text:
                    return response.json().get('csrf_token')
                else:
                    return False
            except:
                return False
        c = C()
        if not c:
            return False
        data = {'url': URL, 'csrf_token': c}
        try:
            response = requests.post(
                'https://klickpin.com/download', data=data)
            if response.status_code == 200:
                so = BeautifulSoup(response.text, 'html.parser')
                url = so.find('a', class_='custom-button-style3')
                if url:
                    return url['href']
                u = so.find('video', id='myVideo')['src']
                if u:
                    return u
            else:
                return False
        except:
            return False
