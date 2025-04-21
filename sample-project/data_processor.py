class DataProcessor:
    # Missing type annotations throughout
    
    def __init__(self, config):
        self.config = config
        # Trailing whitespace - will trigger trailing-whitespace
        self.initialized = True    
    
    def process(self, data):
        # More trailing whitespace
        if self.initialized:  
            # Misspelled word - will trigger codespell
            print("Initialisation complete")
            
            # Process the data based on configuration
            prefix = self.config.get("prefix", "")
            suffix = self.config.get("suffix", "")
            
            # More trailing whitespace
            processed_data = f"{prefix}{data}{suffix}"   
            
            return processed_data
        else:
            # Trailing BOM marker would trigger fix-byte-order-marker
            # This is hard to add directly in the text, but will be simulated
            raise Exception("Not initialized")