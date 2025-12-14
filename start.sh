 || echo "Seed script exited with non-zero code, continuing..."
exec gunicorn "app:create_app()" --bind "0.0.0.0:${PORT:-5000}" --workers 2
