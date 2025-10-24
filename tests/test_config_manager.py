import tempfile
from unittest.mock import patch
from pathlib import Path
import pathlib

import pytest

from bonchcli import config_manager


@pytest.fixture
def mock_config_dir(monkeypatch):
    """Создаёт временную папку вместо ~/.config/bonchcli"""
    temp_dir = tempfile.mkdtemp()  # Создаём временный каталог
    fake_config_path = Path(temp_dir) / "bonchcli"
    fake_config_path.mkdir()  # Создаём пустую директорию
    
    # Подменяем переменную HOME, чтобы приложение искало настройки в `temp_dir`
    monkeypatch.setenv("HOME", temp_dir)
    
    yield fake_config_path  # Передаём путь в тест

    # Очистка (если потребуется)
    # shutil.rmtree(temp_dir)


@pytest.fixture
def mock_home():
    fake_home = Path("/tmp/fake_home")

    with patch.object(Path, "home", return_value=fake_home):
        assert Path.home() == fake_home
        assert Path.home() / ".config/bonchcli" == fake_home / ".config/bonchcli"

    yield fake_home
    
@pytest.fixture
def mock_config_manager(monkeypatch, tmp_path):
    """Фикстура, которая подменяет self.path_config_file на тестовую директорию"""
    fake_home = tmp_path  # Создаём временную директорию

    # Мокаем `Path.home()`, чтобы `self.home_path` смотрел в `tmp_path`
    monkeypatch.setattr(pathlib.Path, "home", lambda: fake_home)

    # Возвращаем замоканный экземпляр ConfigManager
    return config_manager.ConfigManager()


class TestConfigManager:
    @pytest.fixture(autouse=True)
    def setup(self, mock_home):
        self.cm = config_manager.ConfigManager()
        self.cm.path_config_dir = mock_home

#     def test_create_config_file(self):
#         self.cm.create_config_file()
        
    def test_create_config_file(mock_config_manager):
        """Тестируем создание файла в тестовой директории"""
        config_file = mock_config_manager.create_config_file()
        
        assert config_file.exists()  # Файл должен быть создан
        assert config_file.read_text() == "test: value"  # Проверяем содержимое
        assert str(config_file).startswith(str(mock_config_manager.home_path))  # Проверяем путь


    def test_is_config_exists(self):
        assert self.cm.is_config_exists() == False
        self.cm.create_config_file()
        assert self.cm.is_config_exists() == True

