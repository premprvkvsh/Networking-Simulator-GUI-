export async function predict_route(src, dest) {
    const paths = [
        `Device ${src} → Switch 1 → Device ${dest}`,
        `Device ${src} → Hub → Bridge → Device ${dest}`,
        `Device ${src} → Switch → Switch → Device ${dest}`
    ];
    return paths[Math.floor(Math.random() * paths.length)];
}

export async function predict_loss(src, dest) {
    const probability = Math.random();
    return probability.toFixed(2); // 0.00–1.00
}
