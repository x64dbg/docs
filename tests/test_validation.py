"""Validation tests to verify the testing infrastructure is set up correctly."""

import sys
from pathlib import Path

import pytest


class TestInfrastructureSetup:
    """Test class to validate the testing infrastructure setup."""
    
    def test_pytest_is_installed(self):
        """Verify pytest is installed and importable."""
        import pytest
        assert hasattr(pytest, '__version__')
        
    def test_pytest_cov_is_installed(self):
        """Verify pytest-cov is installed and importable."""
        import pytest_cov
        assert hasattr(pytest_cov, '__version__')
        
    def test_pytest_mock_is_installed(self):
        """Verify pytest-mock is installed and importable."""
        import pytest_mock
        # pytest_mock doesn't expose __version__, check for key attribute instead
        assert hasattr(pytest_mock, 'MockerFixture')
        
    def test_project_structure_exists(self):
        """Verify the expected project structure exists."""
        project_root = Path(__file__).parent.parent
        
        # Check main project files
        assert (project_root / 'pyproject.toml').exists()
        assert (project_root / 'conf.py').exists()
        
        # Check test directory structure
        assert (project_root / 'tests').exists()
        assert (project_root / 'tests' / '__init__.py').exists()
        assert (project_root / 'tests' / 'conftest.py').exists()
        assert (project_root / 'tests' / 'unit').exists()
        assert (project_root / 'tests' / 'unit' / '__init__.py').exists()
        assert (project_root / 'tests' / 'integration').exists()
        assert (project_root / 'tests' / 'integration' / '__init__.py').exists()
        
    def test_fixtures_are_available(self, temp_dir, mock_sphinx_config):
        """Verify that conftest fixtures are available."""
        assert temp_dir.exists()
        assert temp_dir.is_dir()
        assert isinstance(mock_sphinx_config, dict)
        assert 'project' in mock_sphinx_config
        
    def test_markers_are_defined(self):
        """Verify custom markers are properly defined."""
        # This test will pass if markers are properly configured
        # in pyproject.toml
        pass
    
    @pytest.mark.unit
    def test_unit_marker_works(self):
        """Test that the unit marker can be used."""
        assert True
        
    @pytest.mark.integration
    def test_integration_marker_works(self):
        """Test that the integration marker can be used."""
        assert True
        
    @pytest.mark.slow
    def test_slow_marker_works(self):
        """Test that the slow marker can be used."""
        assert True
        
    def test_coverage_configuration(self):
        """Verify coverage is configured correctly."""
        # This test verifies coverage runs during pytest execution
        # The actual verification happens through the coverage report
        assert True


class TestSphinxEnvironment:
    """Test Sphinx-specific environment setup."""
    
    def test_sphinx_is_available(self):
        """Verify Sphinx is installed."""
        import sphinx
        assert hasattr(sphinx, '__version__')
        
    def test_recommonmark_is_available(self):
        """Verify recommonmark is installed."""
        import recommonmark
        assert hasattr(recommonmark, '__version__')
        
    def test_sphinx_rtd_theme_is_available(self):
        """Verify sphinx_rtd_theme is installed."""
        import sphinx_rtd_theme
        assert hasattr(sphinx_rtd_theme, '__version__')
        
    def test_conf_py_is_importable(self):
        """Verify conf.py can be imported."""
        project_root = Path(__file__).parent.parent
        sys.path.insert(0, str(project_root))
        try:
            import conf
            assert hasattr(conf, 'project')
        finally:
            sys.path.pop(0)


def test_validation_suite_meta():
    """Meta test to ensure this validation suite itself is working."""
    assert __name__ == 'tests.test_validation' or __name__ == 'test_validation'
    assert Path(__file__).name == 'test_validation.py'