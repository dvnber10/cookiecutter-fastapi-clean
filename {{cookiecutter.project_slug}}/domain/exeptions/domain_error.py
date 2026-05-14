class DomainError(Exception):
    """Excepción base para errores de dominio."""
    def __init__(self, message: str = "Error en el dominio"):
        self.message = message
        super().__init__(self.message)