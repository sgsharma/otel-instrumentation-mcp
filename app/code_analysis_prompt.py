def ask_about_code(code_snippet: str) -> str:
    """Generates a prompt message requesting code analysis and relevant OpenTelemetry documentation.
    
    Args:
        code_snippet: The code snippet to be analyzed
        
    Returns:
        A prompt string asking for code analysis and documentation
    """
    prompt = (
        f"Please analyze this code snippet and provide documentation:\n\n"
        f"Part 1 - Code Analysis:\n"
        f"1. What does this code do?\n"
        f"Part 2 - Documentation:\n"
        f"1. What OpenTelemetry instrumentation would be relevant for this code?\n\n"
        f"2. Provide URLs to relevant OpenTelemetry documentation that explains how to properly instrument this code\n"
        f"3. If applicable, provide links to specific instrumentation examples\n\n"
        f"Code snippet:\n{code_snippet}"
    )

    return prompt
