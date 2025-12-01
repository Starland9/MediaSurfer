import flask
from MediaSurfer import *
app = flask.Flask(__name__)

# Simple OpenAPI JSON schema for the service
OPENAPI_SPEC = {
    "openapi": "3.0.0",
    "info": {
        "title": "MediaSurfer API",
        "version": "1.0.0",
        "description": "API pour télécharger des médias depuis différentes plateformes (YouTube, Instagram, TikTok, Spotify, Facebook, Pinterest)."
    },
    "paths": {
        "/yt": {
            "post": {
                "summary": "Télécharger une resource YouTube",
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "url": {"type": "string"},
                                    "type": {"type": "string", "description": "audio|video"},
                                    "quality": {"type": "string", "description": "par exemple 720p, 1080p"}
                                },
                                "required": ["url", "type"]
                            }
                        }
                    }
                },
                "responses": {
                    "200": {
                        "description": "Succès",
                        "content": {
                            "application/json": {
                                "schema": {"type": "object"},
                                "example": {"status": "success", "ViDeO_LiNk_DeReCT": "https://..."}
                            }
                        }
                    },
                    "400": {"description": "Données invalides"},
                    "500": {"description": "Erreur interne"}
                }
            }
        },
        "/insta": {
            "post": {
                "summary": "Télécharger depuis Instagram",
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {"schema": {"type": "object", "properties": {"url": {"type": "string"}}, "required": ["url"]}}
                    }
                },
                "responses": {"200": {"description": "Succès", "content": {"application/json": {"example": {"status": "success", "ViDeO_LiNk_DeReCT": "https://..."}}}}, "500": {"description": "Erreur"}}
            }
        },
        "/tiktok": {
            "post": {
                "summary": "Télécharger depuis TikTok",
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {"schema": {"type": "object", "properties": {"url": {"type": "string"}}, "required": ["url"]}}
                    }
                },
                "responses": {"200": {"description": "Succès", "content": {"application/json": {"example": {"status": "success", "ViDeO_LiNk_DeReCT": "https://...", "Quality": "Best"}}}}, "500": {"description": "Erreur"}}
            }
        },
        "/spotify": {
            "post": {
                "summary": "Télécharger depuis Spotify",
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {"schema": {"type": "object", "properties": {"url": {"type": "string"}}, "required": ["url"]}}
                    }
                },
                "responses": {"200": {"description": "Succès", "content": {"application/json": {"example": {"status": "success", "AuDiO_LiNk_DeReCT": "https://..."}}}}, "500": {"description": "Erreur"}}
            }
        },
        "/facebook": {
            "post": {
                "summary": "Télécharger depuis Facebook",
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {"schema": {"type": "object", "properties": {"url": {"type": "string"}}, "required": ["url"]}}
                    }
                },
                "responses": {"200": {"description": "Succès", "content": {"application/json": {"example": {"status": "success", "ViDeO_LiNk_DeReCT": "https://...", "Quality": "Normal"}}}}, "500": {"description": "Erreur"}}
            }
        },
        "/pinterest": {
            "post": {
                "summary": "Télécharger depuis Pinterest",
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {"schema": {"type": "object", "properties": {"url": {"type": "string"}}, "required": ["url"]}}
                    }
                },
                "responses": {"200": {"description": "Succès", "content": {"application/json": {"example": {"status": "success", "ViDeO_LiNk_DeReCT": "https://...", "Quality": "Normal"}}}}, "500": {"description": "Erreur"}}
            }
        }
    }
}


@app.route('/openapi.json')
def openapi():
    """Return the OpenAPI JSON spec for the application."""
    return flask.jsonify(OPENAPI_SPEC)


@app.route('/docs')
def docs():
    """Serve a minimal Swagger UI page that loads our `/openapi.json` spec."""
    html = """
    <!doctype html>
    <html lang="fr">
      <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>MediaSurfer - API Docs</title>
        <link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist/swagger-ui.css" />
      </head>
      <body>
        <div id="swagger-ui"></div>
        <script src="https://unpkg.com/swagger-ui-dist/swagger-ui-bundle.js"></script>
        <script>
          window.ui = SwaggerUIBundle({
            url: '/openapi.json',
            dom_id: '#swagger-ui',
            presets: [SwaggerUIBundle.presets.apis],
            layout: 'BaseLayout'
          })
        </script>
      </body>
    </html>
    """
    return html


@app.route('/yt', methods=['POST'])
def yt():
    data = flask.request.get_json()
    try:
        if not data or not 'url' in data or not 'type' in data:
            return flask.jsonify({'status': 'failed', 'reason': 'where data bro??'}), 401
        Url = data.get('url')
        Quality = data.get('quality', None)
        Type = data.get('type')
        x = Yt_ServIcE().Yt_DoWnlOaDeD(url=Url, quality=Quality, type=Type)
        if not x:
            return flask.jsonify({'status': 'failed', 'reason': 'Use Correct Data pLS'}), 400
        elif x.get('status') != 'success':
            return flask.jsonify(x), 500
        return flask.jsonify(x)
    except:
        return flask.jsonify({'status': 'failed', 'reason': 'where data bro??'}), 401


@app.route('/insta', methods=['POST'])
def insta():
    data = flask.request.get_json()
    try:
        if not data or not 'url' in data:
            return flask.jsonify({'status': 'failed', 'reason': 'where data bro??'}), 401
        Url = data.get('url')
        if not Url:
            return flask.jsonify({'status': 'Failed', 'reason': 'Check Your Url !'}), 500
        x = InsTaGrAM_ServIcE().Insta_DoWnlOaDeD(Url)
        if not x:
            return flask.jsonify({'status': 'Failed', 'reason': 'Check Your Url !'}), 500
        return flask.jsonify({'status': 'success', 'ViDeO_LiNk_DeReCT': x})
    except:
        return flask.jsonify({'status': 'failed', 'reason': 'where data bro??'}), 401


@app.route('/tiktok', methods=['POST'])
def tiktok():
    data = flask.request.get_json()
    try:
        if not data or not 'url' in data:
            return flask.jsonify({'status': 'failed', 'reason': 'where data bro??'}), 401
        Url = data.get('url')
        if not Url:
            return flask.jsonify({'status': 'Failed', 'reason': 'Check Your Url !'}), 500
        x = TiKToK_ServIcE().TiKToK_DoWnlOaDeD(Url)
        if not x:
            return flask.jsonify({'status': 'Failed', 'reason': 'Check Your Url !'}), 500
        return flask.jsonify({'status': 'success', 'ViDeO_LiNk_DeReCT': x, 'Quality': 'Best'})
    except:
        return flask.jsonify({'status': 'failed', 'reason': 'where data bro??'}), 401


@app.route('/spotify', methods=['POST'])
def spotify():
    data = flask.request.get_json()
    try:
        if not data or not 'url' in data:
            return flask.jsonify({'status': 'failed', 'reason': 'where data bro??'}), 401
        Url = data.get('url')
        if not Url:
            return flask.jsonify({'status': 'Failed', 'reason': 'Check Your Url !'}), 500
        x = SpOtIfY_ServIcE().SpOtIFy_DoWnlOaDeD(Url)
        print(x)
        if not x:
            return flask.jsonify({'status': 'Failed', 'reason': 'Check Your Url !'}), 500
        return flask.jsonify({'status': 'success', 'AuDiO_LiNk_DeReCT': x})
    except:
        return flask.jsonify({'status': 'failed', 'reason': 'where data bro??'}), 401


@app.route('/facebook', methods=['POST'])
def Facebook():
    data = flask.request.get_json()
    try:
        if not data or not 'url' in data:
            return flask.jsonify({'status': 'failed', 'reason': 'where data bro??'}), 401
        Url = data.get('url')
        if not Url:
            return flask.jsonify({'status': 'Failed', 'reason': 'Check Your Url !'}), 500
        x = FaCeBoOk_ServIcE().FaCeBoOk_DoWnlOaDeD(Url)
        if not x:
            return flask.jsonify({'status': 'Failed', 'reason': 'Check Your Url !'}), 500
        return flask.jsonify({'status': 'success', 'ViDeO_LiNk_DeReCT': x, 'Quality': 'Normal'})
    except:
        return flask.jsonify({'status': 'failed', 'reason': 'where data bro??'}), 401


@app.route('/pinterest', methods=['POST'])
def Pinterest():
    data = flask.request.get_json()
    try:
        if not data or not 'url' in data:
            return flask.jsonify({'status': 'failed', 'reason': 'where data bro??'}), 401
        Url = data.get('url')
        if not Url:
            return flask.jsonify({'status': 'Failed', 'reason': 'Check Your Url !'}), 500
        x = PiNteResT_ServIcE().PiNteResT_DoWnlOaDeD(Url)
        if not x:
            return flask.jsonify({'status': 'Failed', 'reason': 'Check Your Url !'}), 500
        return flask.jsonify({'status': 'success', 'ViDeO_LiNk_DeReCT': x, 'Quality': 'Normal'})
    except:
        return flask.jsonify({'status': 'failed', 'reason': 'where data bro??'}), 401


if __name__ == "__main__":
    app.run()
