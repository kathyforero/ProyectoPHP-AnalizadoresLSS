// Definir las dos variables
$num1 = 10;
$num2 = 5;

// Función que realiza las operaciones
function operaciones($a, $b) {
    // Calcular cada operación
    $suma = $a + $b;
    $resta = $a - $b;
    $multiplicacion = $a * $b;

    // Usar un 'if' para verificar la división por cero
    if ($b != 0) {
        $division = $a / $b;
    } else {
        $division = 'No se puede dividir por cero';
    }

    // Devolver los resultados en un array
    return [
        "suma" => $suma,
        "resta" => $resta,
        "multiplicacion" => $multiplicacion,
        "division" => $division
    ];
}