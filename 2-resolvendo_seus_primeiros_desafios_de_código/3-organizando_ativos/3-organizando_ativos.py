DEPLOY_ENVIRONMENT = True


def getAssetsQuantityFromUser():
    if DEPLOY_ENVIRONMENT:
        print("Insira a quantidade de ativos:")
    assetsQuantity = int(input())
    return assetsQuantity


def getAssetsFromUser(numberOfAssets):
    assetsArray = []

    for _ in range(numberOfAssets):
        if DEPLOY_ENVIRONMENT:
            print("Insira um código de ativo:")
        codigoAtivo = input()
        assetsArray.append(codigoAtivo)

    return assetsArray


def orderAssets(assetsArray):
    assetsArray.sort(key=str.lower)
    return assetsArray


def printAssets(array):
    if DEPLOY_ENVIRONMENT:
        print("Ativos ordenados:")
    for item in array:
        print(item)


def main():
    quantidadeAtivos = getAssetsQuantityFromUser()
    ativos = getAssetsFromUser(quantidadeAtivos)
    orderedAssets = orderAssets(ativos)
    printAssets(orderedAssets)


main()
