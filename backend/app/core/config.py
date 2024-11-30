from typing import Any, Dict, Optional

from pydantic import validator
from pydantic_settings import BaseSettings


# 应用程序配置类,继承自BaseSettings以支持从环境变量加载配置
class Settings(BaseSettings):
    # 项目基本配置
    PROJECT_NAME: str = "Desktop Clock Hub"  # 项目名称
    API_V1_STR: str = "/api/v1"  # API版本路径前缀

    # SQLite配置
    SQLITE_DB: str = "sql_app.db"
    SQLALCHEMY_DATABASE_URI: Optional[str] = None

    # 数据库URI验证器,用于构建完整的数据库连接URI
    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        sqlite_db = values.get("SQLITE_DB")
        return f"sqlite+aiosqlite:///{sqlite_db}"

    # JWT认证配置
    JWT_SECRET_KEY: str  # JWT密钥
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 访问令牌过期时间,默认8天

    # Redis配置
    REDIS_HOST: str = "localhost"  # Redis服务器地址
    REDIS_PORT: int = 6379  # Redis端口号

    # 配置类设置
    class Config:
        case_sensitive = True  # 配置键值大小写敏感
        env_file = ".env"  # 从.env文件加载环境变量


# 创建全局配置实例
settings = Settings()
