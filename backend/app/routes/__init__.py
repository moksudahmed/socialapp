# app/routes/__init__.py

from .auth import auth_bp
from .posts import posts_bp
from .comments import comments_bp
from .likes import likes_bp
from .photos import photos_bp
from .other import other_bp  # Import the other_bp blueprint

# Register all the blueprints
__all__ = ['auth_bp', 'posts_bp', 'comments_bp', 'likes_bp', 'photos_bp', 'other_bp']
