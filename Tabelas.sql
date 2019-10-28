CREATE TABLE IF NOT EXISTS `pacotes`
(
 `codigo`       bigint NOT NULL AUTO_INCREMENT ,
 `peso`         double NOT NULL ,
 `altura`       double NOT NULL ,
 `comprimento`  double NOT NULL ,
 `profundidade` double NOT NULL ,
 `origem`       varchar(100) NOT NULL ,
 `destino`      varchar(100) NOT NULL ,
 `fragil`       tinyint NOT NULL ,
 `expresso`     tinyint NOT NULL ,
 `preco`        double NOT NULL ,
 `remetente`    varchar(100) NOT NULL ,
 `destinatario` varchar(100) NOT NULL ,

PRIMARY KEY (`codigo`)
)AUTO_INCREMENT = 1000000000000;


CREATE TABLE IF NOT EXISTS `historico`
(
 `codDeAtualizacao` bigint NOT NULL AUTO_INCREMENT,
 `codigo`      bigint NOT NULL ,
 `atualizacao` text NOT NULL ,
  PRIMARY KEY (`codDeAtualizacao`),
  FOREIGN KEY (`codigo`) REFERENCES `pacotes`(`codigo`)
);

CREATE TABLE IF NOT EXISTS `pessoa`
(
 `CPF`        varchar(11) NOT NULL ,
 `nome`       varchar(100) NOT NULL ,
 `endereco`   text NOT NULL ,
 `sexo`       char NOT NULL ,
 `nascimento` date NOT NULL ,
 `email`      varchar(100) NOT NULL ,
 `usuario`    varchar(100) NOT NULL UNIQUE ,
 `senha`      varchar(100) NOT NULL ,
 `tipodeUser` int NOT NULL ,

PRIMARY KEY (`CPF`)
);

CREATE TABLE IF NOT EXISTS `rastreia`
(
 `idRastreio` bigint NOT NULL AUTO_INCREMENT ,
 `CPF`        varchar(11) NOT NULL ,
 `codigo`     bigint NOT NULL ,

PRIMARY KEY (`idRastreio`),
FOREIGN KEY (`CPF`) REFERENCES `pessoa` (`CPF`),
FOREIGN KEY (`codigo`) REFERENCES `pacotes` (`codigo`)
);

/* ver os pacotes associados a um cpf*/
select pacotes.* from pacotes,rastreia,pessoa where pessoa.CPF=rastreia.CPF AND pacotes.codigo=rastreia.codigo AND pessoa.CPF='07665411148';
/* historico associado a um pacote*/
select atualizacao from historico where codigo=1000000000001;