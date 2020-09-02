from __future__ import unicode_literals

SECRET_KEY = {{ secret_key }}
NEVERCACHE_KEY = {{ nevercache_key }}
ALLOWED_HOSTS = [{% for domain in domains}"{{ domain }}",{% endfor %}]

DATABASES = {
	"default" : {
		# Ends with db type
		"ENGINE": "django.dev.backends.postgresql_psycopg2",
		# db name or path
		"NAME": "{{ proj_name }}",
		# user
		"USER": "{{ proj_name }}",
		# password
		"PASSWORD": "{{ db_pass }}",
		# host
		"HOST": "127.0.0.1",
		# port
		"PORT": "",
	}
}

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")

CACHE_MIDDLEWARE_SECONDS = 60

CACHE_MIDDLEWARE_KEY_PREFIX = "{{ proj_name }}"

CACHES = {
	"default": {
		"BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
		"LOCATION": "127.0.0.1:11211",
	}
}

SESSION_ENGINE = "django.contrib.sessions.backend.cache"