# test_nftnode.py
"""
Tests for NFTNode module.
"""

import unittest
from nftnode import NFTNode

class TestNFTNode(unittest.TestCase):
    """Test cases for NFTNode class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NFTNode()
        self.assertIsInstance(instance, NFTNode)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NFTNode()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
