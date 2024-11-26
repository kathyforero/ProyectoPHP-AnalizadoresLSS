// Array asociativo de frutas con su precio unitario
$frutas = [
    "manzana" => 2.5,
    "banana" => 1.8,
    "naranja" => 3.0,
    "pera" => 2.2,
    "uva" => 4.0
];

// Función para calcular el total a pagar
function calcularTotal($nombreFruta, $cantidad, $arregloFrutas) {
    // Verificar si la fruta existe en el arreglo
    if (array_key_exists($nombreFruta, $arregloFrutas)) {
        // Calcular el total
        $precioUnitario = $arregloFrutas[$nombreFruta];
        $total = $precioUnitario * $cantidad;
        return $total;
    } else {
        return "La fruta no está disponible.";
    }
}