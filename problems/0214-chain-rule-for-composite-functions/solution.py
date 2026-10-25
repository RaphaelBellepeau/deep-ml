import numpy as np

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
    """
    Computes the gradient of a composition of functions using the chain rule,
    where functions[0] is the outermost function and the last is the innermost.
    """
    # Helper for forward pass value of a single function
    def forward(f, val):
        match f:
            case 'sin':
                return np.sin(val)
            case 'square':
                return val ** 2
            case 'exp':
                return np.exp(val)
            case 'log':
                return np.log(val)
            case _:
                raise ValueError(f"Unknown function: {f}")

    # Helper for the derivative of a single function evaluated at val
    def derivative(f, val):
        match f:
            case 'sin':
                return np.cos(val)
            case 'square':
                return 2 * val
            case 'exp':
                return np.exp(val)
            case 'log':
                return 1 / val
            case _:
                raise ValueError(f"Unknown function: {f}")

    # 1. Compute intermediate values for each nested layer from inside out
    # For ['exp', 'sin', 'square'] and x = 0.5:
    # - square(0.5) = 0.25
    # - sin(0.25) = 0.24740395
    # - exp(0.24740395) = 1.28070836
    
    values = [x]
    current = x
    for f in reversed(functions):
        current = forward(f, current)
        values.append(current)
    
    # values will be: [0.5 (input), 0.25 (after square), 0.2474... (after sin), 1.2807... (after exp)]
    # We want to multiply the derivatives of each function evaluated at its respective input.
    # Functions correspond from left to right: functions[0] ('exp') acts on the output of 'sin', etc.
    
    # Let's compute the product of derivatives:
    # derivative of exp at (sin(square(0.5))) * derivative of sin at (square(0.5)) * derivative of square at (0.5)
    
    grad = 1.0
    for idx, f in enumerate(functions):
        # The input to the function at index `idx` is stored in `values[len(functions) - 1 - idx]`
        input_val = values[len(functions) - 1 - idx]
        grad *= derivative(f, input_val)
        
    return grad