from contextlib import contextmanager
import tls_client
import json

from characterai.pyasynccai import PyAsyncCAI

__all__ = ['PyCAI', 'PyAsyncCAI']

class PyCAI:
    def __init__(
        self, token: str = None, plus: bool = False
    ):
        self.token = token

        if plus: sub = 'plus'
        else: sub = 'beta'

        self.session = tls_client.Session(
            client_identifier='chrome112'
        )

        setattr(self.session, 'url', f'https://{sub}.character.ai/')
        setattr(self.session, 'yJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVqYmxXUlVCWERJX0dDOTJCa2N1YyJ9.eyJpc3MiOiJodHRwczovL2NoYXJhY3Rlci1haS51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTA2OTIwNjE5MzEyNDE1ODU4MDUiLCJhdWQiOlsiaHR0cHM6Ly9hdXRoMC5jaGFyYWN0ZXIuYWkvIiwiaHR0cHM6Ly9jaGFyYWN0ZXItYWkudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTY5NTM2OTExMSwiZXhwIjoxNjk3OTYxMTExLCJhenAiOiJkeUQzZ0UyODFNcWdJU0c3RnVJWFloTDJXRWtucVp6diIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwifQ.0OSB__3Nl1fHTKg3b1sF_ByfY8I8OAydb3awfXHXhZ1leAwhpG-4T8g5NGykiaqaMZ-YvHm9wOpd1ri2S4BGAHGH0Xik25fWd5HhOe2LESX_VQKFBnJr9O1PVMfGdi0aff-97ZE_-4FTpsK7W8-IM2eL_scTwIsmbTDCpBrFBir2cyQSv8NERQJdz28XBNhdil2zcZUCeXGIHJJs4_1fEqmAVk5AGcmAfOlC6ViSnZGfaRHVmznEz-eAmgtVStUOUKt1he-TQF5RRmkD3xHDCSAJw0O0Vxtv-9bQDnhH2Mk3VTLKFjXA_TV0gXayQTa_pVoT4SzeegL8-T6ZfoTRAw","id_token":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVqYmxXUlVCWERJX0dDOTJCa2N1YyJ9.eyJnaXZlbl9uYW1lIjoiUkNTIiwiZmFtaWx5X25hbWUiOiJYWiIsIm5pY2tuYW1lIjoicmNzeHo2NDkiLCJuYW1lIjoiUkNTIFhaIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FDZzhvY0lYbGpRdW11SWlQTjdwLUoxUk1HNjZ0ODZzTzJhMG9DcW93RTlZVDFzaj1zOTYtYyIsImxvY2FsZSI6ImlkIiwidXBkYXRlZF9hdCI6IjIwMjMtMDktMjJUMDc6NTE6NDQuNDUyWiIsImVtYWlsIjoicmNzeHo2NDlAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImlzcyI6Imh0dHBzOi8vY2hhcmFjdGVyLWFpLnVzLmF1dGgwLmNvbS8iLCJhdWQiOiJkeUQzZ0UyODFNcWdJU0c3RnVJWFloTDJXRWtucVp6diIsImlhdCI6MTY5NTM2OTExMSwiZXhwIjoxNjk4OTY5MTExLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExMDY5MjA2MTkzMTI0MTU4NTgwNSIsImF1dGhfdGltZSI6MTY5NTM2OTEwNCwic2lkIjoiTVh2TnljZV8zdlFYWTBIMUQ4NVZuQl9neDBFWXllRzkiLCJub25jZSI6Ik55MVFUMjlQTWxwbmFsTmlkME41YUhwUU9VZ3hZVFJWV1RNNFdVeEZRazlPT1RCMlVuQkNVVjl1U0E9PSJ9.GHALnhshn2c1U_VDjFY4pC3p51QqwdJ21TBLl33rd9PBDwBYO0eYKjmDkT8fTcxW6n9CdZTiVb4V5PIPdHnXAjGPNp8fvCR7Kfzc39Fc8_9Rl9wB5Q-Ob3y1b7jdyexC7hivyffiqzz0LrCIBTOe9pDemY2UA-9f3eFkYuACudplhR0UINc00rjA2fHweke_Asn7has_9gR95kzSZmOWoF_X3xPwnprXyiDagfg3UzLj-ixa7KBBLPC6epf_-3U5JtQ3J1C2sDUtZsbH7MHSjuemTLyoUh_4KedsbChEBgUKN053E6vqZbmBuXtxNtrf0dhABfXWoonHku-c_rvmWQ","scope":"openid profile email offline_access","expires_in":2592000,"token_type":"Bearer","decodedToken":{"encoded":{"header":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVqYmxXUlVCWERJX0dDOTJCa2N1YyJ9","payload":"eyJnaXZlbl9uYW1lIjoiUkNTIiwiZmFtaWx5X25hbWUiOiJYWiIsIm5pY2tuYW1lIjoicmNzeHo2NDkiLCJuYW1lIjoiUkNTIFhaIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FDZzhvY0lYbGpRdW11SWlQTjdwLUoxUk1HNjZ0ODZzTzJhMG9DcW93RTlZVDFzaj1zOTYtYyIsImxvY2FsZSI6ImlkIiwidXBkYXRlZF9hdCI6IjIwMjMtMDktMjJUMDc6NTE6NDQuNDUyWiIsImVtYWlsIjoicmNzeHo2NDlAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImlzcyI6Imh0dHBzOi8vY2hhcmFjdGVyLWFpLnVzLmF1dGgwLmNvbS8iLCJhdWQiOiJkeUQzZ0UyODFNcWdJU0c3RnVJWFloTDJXRWtucVp6diIsImlhdCI6MTY5NTM2OTExMSwiZXhwIjoxNjk4OTY5MTExLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExMDY5MjA2MTkzMTI0MTU4NTgwNSIsImF1dGhfdGltZSI6MTY5NTM2OTEwNCwic2lkIjoiTVh2TnljZV8zdlFYWTBIMUQ4NVZuQl9neDBFWXllRzkiLCJub25jZSI6Ik55MVFUMjlQTWxwbmFsTmlkME41YUhwUU9VZ3hZVFJWV1RNNFdVeEZRazlPT1RCMlVuQkNVVjl1U0E9PSJ9","signature":"GHALnhshn2c1U_VDjFY4pC3p51QqwdJ21TBLl33rd9PBDwBYO0eYKjmDkT8fTcxW6n9CdZTiVb4V5PIPdHnXAjGPNp8fvCR7Kfzc39Fc8_9Rl9wB5Q-Ob3y1b7jdyexC7hivyffiqzz0LrCIBTOe9pDemY2UA-9f3eFkYuACudplhR0UINc00rjA2fHweke_Asn7has_9gR95kzSZmOWoF_X3xPwnprXyiDagfg3UzLj-ixa7KBBLPC6epf_-3U5JtQ3J1C2sDUtZsbH7MHSjuemTLyoUh_4KedsbChEBgUKN053E6vqZbmBuXtxNtrf0dhABfXWoonHku-c_rvmWQ"},"header":{"alg":"RS256","typ":"JWT","kid":"EjblWRUBXDI_GC92Bkcuc"},"claims":{"__raw":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVqYmxXUlVCWERJX0dDOTJCa2N1YyJ9.eyJnaXZlbl9uYW1lIjoiUkNTIiwiZmFtaWx5X25hbWUiOiJYWiIsIm5pY2tuYW1lIjoicmNzeHo2NDkiLCJuYW1lIjoiUkNTIFhaIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FDZzhvY0lYbGpRdW11SWlQTjdwLUoxUk1HNjZ0ODZzTzJhMG9DcW93RTlZVDFzaj1zOTYtYyIsImxvY2FsZSI6ImlkIiwidXBkYXRlZF9hdCI6IjIwMjMtMDktMjJUMDc6NTE6NDQuNDUyWiIsImVtYWlsIjoicmNzeHo2NDlAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImlzcyI6Imh0dHBzOi8vY2hhcmFjdGVyLWFpLnVzLmF1dGgwLmNvbS8iLCJhdWQiOiJkeUQzZ0UyODFNcWdJU0c3RnVJWFloTDJXRWtucVp6diIsImlhdCI6MTY5NTM2OTExMSwiZXhwIjoxNjk4OTY5MTExLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExMDY5MjA2MTkzMTI0MTU4NTgwNSIsImF1dGhfdGltZSI6MTY5NTM2OTEwNCwic2lkIjoiTVh2TnljZV8zdlFYWTBIMUQ4NVZuQl9neDBFWXllRzkiLCJub25jZSI6Ik55MVFUMjlQTWxwbmFsTmlkME41YUhwUU9VZ3hZVFJWV1RNNFdVeEZRazlPT1RCMlVuQkNVVjl1U0E9PSJ9.GHALnhshn2c1U_VDjFY4pC3p51QqwdJ21TBLl33rd9PBDwBYO0eYKjmDkT8fTcxW6n9CdZTiVb4V5PIPdHnXAjGPNp8fvCR7Kfzc39Fc8_9Rl9wB5Q-Ob3y1b7jdyexC7hivyffiqzz0LrCIBTOe9pDemY2UA-9f3eFkYuACudplhR0UINc00rjA2fHweke_Asn7has_9gR95kzSZmOWoF_X3xPwnprXyiDagfg3UzLj-ixa7KBBLPC6epf_-3U5JtQ3J1C2sDUtZsbH7MHSjuemTLyoUh_4KedsbChEBgUKN053E6vqZbmBuXtxNtrf0dhABfXWoonHku-c_rvmWQ', token)

        self.user = self.user(token, self.session)
        self.post = self.post(token, self.session)
        self.character = self.character(token, self.session)
        self.chat = self.chat(token, self.session)

    def request(
        url: str, session: tls_client.Session,
        *, token: str = None, method: str = 'GET',
        data: dict = None, split: bool = False,
        neo: bool = False
    ):
        if neo:
            link = f'https://neo.character.ai/{url}'
        else:
            link = f'{session.url}{url}'

        if token == None:
            key = session.token
        else:
            key = token

        headers = {
            'Authorization': f'Token {key}'
        }

        if method == 'GET':
            response = session.get(
                link, headers=headers
            )

        elif method == 'POST':
            response = session.post(
                link, headers=headers, json=data
            )

        elif method == 'PUT':
            response = session.put(
                link, headers=headers, json=data
            )

        if split:
            data = json.loads(response.text.split('\n')[-2])
        else:
            data = response.json()

        if str(data).startswith("{'command': 'neo_error'"):
            raise errors.ServerError(data['comment'])
        elif str(data).startswith("{'detail': 'Auth"):
            raise errors.AuthError('Invalid token')
        elif str(data).startswith("{'status': 'Error"):
            raise errors.ServerError(data['status'])
        elif str(data).startswith("{'error'"):
            raise errors.ServerError(data['error'])
        else:
            return data

    def ping(self):
        return self.session.get(
            'https://neo.character.ai/ping/'
        ).json()

    class user:
        """Responses from site for user info

        user.info()
        user.get_profile('USERNAME')
        user.followers()
        user.following()
        user.update('USERNAME')

        """
        def __init__(
            self, token: str, session: tls_client.Session
        ):
            self.token = token
            self.session = session

        def info(self, *, token: str = None):
            return PyCAI.request(
                'chat/user/', self.session, token=token
            )

        def get_profile(
            self, username: str, *,
            token: str = None
        ):
            return PyCAI.request(
                'chat/user/public/', self.session,
                token=token, method='POST',
                data={
                    'username': username
                }
            )

        def followers(self, *, token: str = None):
            return PyCAI.request(
                'chat/user/followers/', self.session, token=token
            )

        def following(self, *, token: str = None):
            return PyCAI.request(
                'chat/user/following/', self.session, token=token
            )
        
        def recent(self, *, token: str = None):
            return PyCAI.request(
                'chat/characters/recent/', self.session, token=token
            )

        def characters(self, *, token: str = None):
            return PyCAI.request(
                'chat/characters/?scope=user',
                self.session, token=token
            )

        def update(
            self, username: str,
            *, token: str = None,
            **kwargs
        ):
            return PyCAI.request(
                'chat/user/update/', self.session,
                token=token, method='POST',
                data={
                    'username': username,
                    **kwargs
                }
            )

    class post:
        """Just a responses from site for posts
        
        post.get_post('POST_ID')
        post.my_posts()
        post.get_posts('USERNAME')
        post.upvote('POST_ID')
        post.undo_upvote('POST_ID')
        post.send_comment('POST_ID', 'TEXT')
        post.delete_comment('MESSAGE_ID', 'POST_ID')
        post.create('HISTORY_ID', 'TITLE')
        post.delete('POST_ID')

        """
        def __init__(
            self, token: str, session: tls_client.Session
        ):
            self.token = token
            self.session = session

        def get_post(
            self, post_id: str
        ):
            return PyCAI.request(
                f'chat/post/?post={post_id}',
                self.session
            )

        def my(
            self, *, posts_page: int = 1,
            posts_to_load: int = 5, token: str = None
        ):
            return PyCAI.request(
                f'chat/posts/user/?scope=user&page={posts_page}'
                f'&posts_to_load={posts_to_load}/',
                self.session
            )

        def get_posts(
            self, username: str, *,
            posts_page: int = 1, posts_to_load: int = 5,
        ):
            return PyCAI.request(
                f'chat/posts/user/?username={username}'
                f'&page={posts_page}&posts_to_load={posts_to_load}/',
                self.session
            )

        def upvote(
            self, post_external_id: str,
            *, token: str = None
        ):
            return PyCAI.request(
                'chat/post/upvote/', self.session,
                token=token, method='POST',
                data={
                    'post_external_id': post_external_id
                }
            )

        def undo_upvote(
            self, post_external_id: str,
            *, token: str = None
        ):
            return PyCAI.request(
                'chat/post/undo-upvote/', self.session,
                token=token, method='POST',
                data={
                    'post_external_id': post_external_id
                }
            )

        def send_comment(
            self, post_id: str, text: str, *,
            parent_uuid: str = None, token: str = None
        ):
            return PyCAI.request(
                'chat/comment/create/', self.session,
                token=token, method='POST',
                data={
                    'post_external_id': post_id,
                    'text': text,
                    'parent_uuid': parent_uuid
                }
            )

        def delete_comment(
            self, message_id: int, post_id: str,
            *, token: str = None
        ):
            return PyCAI.request(
                'chat/comment/delete/', self.session,
                token=token, method='POST',
                data={
                    'external_id': message_id,
                    'post_external_id': post_id
                }
            )

        def create(
            self, post_type: str, external_id: str,
            title: str, text: str = '',
            post_visibility: str = 'PUBLIC',
            token: str = None, **kwargs
        ):
            if post_type == 'POST':
                post_link = 'chat/post/create/'
                data = {
                    'post_title': title,
                    'topic_external_id': external_id,
                    'post_text': text,
                    **kwargs
                }
            elif post_type == 'CHAT':
                post_link = 'chat/chat-post/create/'
                data = {
                    'post_title': title,
                    'subject_external_id': external_id,
                    'post_visibility': post_visibility,
                    **kwargs
                }
            else:
                raise errors.PostTypeError('Invalid post_type')

            return PyCAI.request(
                post_link, self.session,
                token=token, method='POST'
            )

        def delete(
            self, post_id: str, *,
            token: str = None
        ):
            return PyCAI.request(
                'chat/post/delete/', self.session,
                token=token, method='POST',
                data={
                    'external_id': post_id
                }
            )

        def get_topics(self):
            return PyCAI.request(
                'chat/topics/', self.session
            )

        def feed(
            self, topic: str, num: int = 1, 
            load: int = 5, sort: str = 'top', *,
            token: str = None
        ):
            return PyCAI.request(
                f'chat/posts/?topic={topic}&page={num}'
                f'&posts_to_load={load}&sort={sort}',
                self.session, token=token
            )

    class character:
        """Just a responses from site for characters

        character.create()
        character.update()
        character.trending()
        character.recommended()
        character.categories()
        character.info('CHAR')
        character.search('QUERY')
        character.voices()

        """
        def __init__(
            self, token: str, session: tls_client.Session
        ):
            self.token = token
            self.session = session

        def create(
            self, greeting: str, identifier: str,
            name: str, *, avatar_rel_path: str = '',
            base_img_prompt: str = '', categories: list = [],
            copyable: bool = True, definition: str = '',
            description: str = '', title: str = '',
            img_gen_enabled: bool = False,
            visibility: str = 'PUBLIC',
            token: str = None, **kwargs
        ):
            return PyCAI.request(
                '../chat/character/create/', self.session,
                token=token, method='POST',
                data={
                    'greeting': greeting,
                    'identifier': identifier,
                    'name': name,
                    'avatar_rel_path': avatar_rel_path,
                    'base_img_prompt': base_img_prompt,
                    'categories': categories,
                    'copyable': copyable,
                    'definition': definition,
                    'description': description,
                    'img_gen_enabled': img_gen_enabled,
                    'title': title,
                    'visibility': visibility,
                    **kwargs
                }
            )

        def update(
            self, external_id: str, greeting: str,
            identifier: str, name: str, title: str = '',
            categories: list = [], definition: str = '',
            copyable: bool = True, description: str = '',
            visibility: str = 'PUBLIC', *,
            token: str = None, **kwargs
        ):
            return PyCAI.request(
                '../chat/character/update/', self.session,
                token=token, method='POST',
                data={
                    'external_id': external_id,
                    'name': name,
                    'categories': categories,
                    'title': title,
                    'visibility': visibility,
                    'copyable': copyable,
                    'description': description,
                    'greeting': greeting,
                    'definition': definition,
                    **kwargs
                }
            )
        
        def trending(self):
            return PyCAI.request(
                'chat/characters/trending/',
                self.session
            )

        def recommended(
            self, *, token: str = None
        ):
            return PyCAI.request(
                'chat/characters/recommended/',
                self.session, token=token
            )

        def categories(self):
            return PyCAI.request(
                'chat/character/categories/',
                self.session
            )

        def info(
            self, char: str, *,
            token: str = None,
        ):
            return PyCAI.request(
                'chat/character/', self.session,
                token=token, method='POST',
                data={
                    'external_id': char
                }
            )

        def search(
            self, query: str, *,
            token: str = None
        ):
            return PyCAI.request(
                f'chat/characters/search/?query={query}/',
                self.session, token=token
            )

        def voices(self):
            return PyCAI.request(
                'chat/character/voices/',
                self.session
            )

    class chat:
        """Managing a chat with a character

        chat.create_room('CHARACTERS', 'NAME', 'TOPIC')
        chat.rate(NUM, 'HISTORY_ID', 'MESSAGE_ID')
        chat.next_message('CHAR', 'MESSAGE')
        chat.get_histories('CHAR')
        chat.get_history('HISTORY_EXTERNAL_ID')
        chat.get_chat('CHAR')
        chat.send_message('CHAR', 'MESSAGE')
        chat.delete_message('HISTORY_ID', 'UUIDS_TO_DELETE')
        chat.new_chat('CHAR')

        """
        def __init__(
            self, token: str, session: tls_client.Session
        ):
            self.token = token
            self.session = session

        def create_room(
            self, characters: list, name: str,
            topic: str = '', *, token: str = None,
            **kwargs
        ):
            return PyCAI.request(
                '../chat/room/create/', self.session,
                token=token, method='POST',
                data={
                    'characters': characters,
                    'name': name,
                    'topic': topic,
                    'visibility': 'PRIVATE',
                    **kwargs
                }
            )

        def rate(
            self, rate: int, history_id: str,
            message_id: str, *, token: str = None,
            **kwargs
        ):
            if rate == 0: label = [234, 238, 241, 244] #Terrible
            elif rate == 1: label = [235, 237, 241, 244] #Bad
            elif rate == 2: label = [235, 238, 240, 244] #Good
            elif rate == 3: label = [235, 238, 241, 243] #Fantastic
            else: raise errors.LabelError('Wrong Rate Value')

            return PyCAI.request(
                'chat/annotations/label/', self.session,
                token=token, method='PUT',
                data={
                    'label_ids': label,
                    'history_external_id': history_id,
                    'message_uuid': message_id,
                    **kwargs
                }
            )

        def next_message(
            self, history_id: str, parent_msg_uuid: str,
            tgt: str, *, token: str = None, **kwargs
        ):
            response = PyCAI.request(
                'chat/streaming/', self.session,
                token=token, method='POST', split=True,
                data={
                    'history_external_id': history_id,
                    'parent_msg_uuid': parent_msg_uuid,
                    'tgt': tgt,
                    **kwargs
                }
            )

        def get_histories(
            self, char: str, *, number: int = 50,
            token: str = None
        ):
            return PyCAI.request(
                'chat/character/histories_v2/', self.session,
                token=token, method='POST',
                data={'external_id': char, 'number': number},
            )

        def get_history(
            self, history_id: str = None,
            *, token: str = None
        ):
            return PyCAI.request(
                'chat/history/msgs/user/?'
                f'history_external_id={history_id}',
                self.session, token=token
            )

        def get_chat(
            self, char: str = None, *,
            token: str = None, **kwargs
        ):
            return PyCAI.request(
                'chat/history/continue/', self.session,
                token=token, method='POST',
                data={
                    'character_external_id': char,
                    **kwargs
                }
            )

        def send_message(
            self, history_id: str, tgt: str, text: str,
            *, token: str = None, **kwargs
        ):
            return PyCAI.request(
                'chat/streaming/', self.session,
                token=token, method='POST', split=True,
                data={
                    'history_external_id': history_id,
                    'tgt': tgt,
                    'text': text,
                    **kwargs
                }
            )

        def delete_message(
            self, history_id: str, uuids_to_delete: list,
            *, token: str = None, **kwargs
        ):
            return PyCAI.request(
                'chat/history/msgs/delete/', self.session,
                token=token, method='POST',
                data={
                    'history_id': history_id,
                    'uuids_to_delete': uuids_to_delete,
                    **kwargs
                }
            )

        def new_chat(
            self, char: str, *, token: str = None
        ):
            return PyCAI.request(
                'chat/history/create/', self.session,
                token=token, method='POST',
                data={
                    'character_external_id': char
                }
            )
