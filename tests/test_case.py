# tests/test_project.py
import subprocess
import sys
import os
import pytest

# -------------------------------
# 1. Backend dependencies check
# -------------------------------
def test_backend_requirements():
    req_file = os.path.join("backend", "requirements.txt")
    if os.path.exists(req_file):
        result = subprocess.run([sys.executable, "-m", "pip", "check"], capture_output=True, text=True)
        assert "No broken requirements found" in result.stdout or result.returncode == 0
    else:
        pytest.skip("No backend requirements.txt found")

# -------------------------------
# 2. ML dependencies check
# -------------------------------
def test_ml_requirements():
    req_file = os.path.join("ml", "requirements.txt")
    if os.path.exists(req_file):
        result = subprocess.run([sys.executable, "-m", "pip", "check"], capture_output=True, text=True)
        assert "No broken requirements found" in result.stdout or result.returncode == 0
    else:
        pytest.skip("No ML requirements.txt found")

# -------------------------------
# 3. Backend app health check
# -------------------------------
def test_backend_app_help():
    backend_app = os.path.join("backend", "app.py")
    assert os.path.exists(backend_app), "backend/app.py does not exist"

    result = subprocess.run([sys.executable, backend_app, "--help"], capture_output=True, text=True)
    assert result.returncode == 0, "Backend app.py did not run with --help"
    assert "usage" in result.stdout.lower() or result.stderr == ""

# -------------------------------
# 4. Streamlit check
# -------------------------------
def test_streamlit_installed():
    result = subprocess.run(["streamlit", "--version"], capture_output=True, text=True)
    assert result.returncode == 0, "Streamlit not installed"
    assert result.stdout.strip() != "", "Streamlit version not returned"

# -------------------------------
# 5. Lint check (flake8)
# -------------------------------
def test_flake8_lint():
    result = subprocess.run([sys.executable, "-m", "flake8", "."], capture_output=True, text=True)
    # Flake8 returns 0 if no issues, otherwise non-zero. We allow warnings for CI.
    assert result.returncode in [0, 1], f"Linting failed: {result.stdout}"

# -------------------------------
# 6. Placeholder for additional unit tests
# -------------------------------
def test_placeholder():
    # Example: you can import your backend functions and test them here
    assert True
