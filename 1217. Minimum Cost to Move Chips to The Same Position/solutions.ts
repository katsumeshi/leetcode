function minCostToMoveChips(position: number[]): number {
    const d = [0, 0]
    for(let i = 0; i < position.length; i++) {
        d[position[i]%2] += 1
    }
    return Math.min(d[0], d[1])
};
