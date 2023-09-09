USE mydb;

INSERT INTO `myapp_tiposrecursos` VALUES (1,'elevador','Dispositivo vertical para transporte entre diferentes níveis de um edifício.'),(2,'plataforma elevatória','Equipamento que eleva pessoas ou objetos para superar desníveis.'),(3,'ponto de taxi','Local designado para pegar ou deixar passageiros de táxi.'),(4,'sinalização','Conjunto de sinais visuais ou auditivos para orientação e segurança.'),(5,'rampas','Superfícies inclinadas que facilitam o acesso a áreas elevadas ou rebaixadas.'),(6,'corrimões','Estruturas de apoio para garantir segurança ao subir ou descer escadas.'),(7,'portas amplas','Entradas com aberturas largas para permitir fácil acesso a espaços internos.'),(8,'calçada acessível','Caminho para pedestres adaptado para pessoas com deficiência.'),(9,'vagas preferenciais','Estacionamento reservado para pessoas com necessidades especiais.'),(10,'banheiro família','Instalação sanitária projetada para uso de famílias com crianças pequenas.'),(11,'barras de apoio','Estruturas instaladas para ajudar pessoas com mobilidade reduzida a se apoiarem.'),(12,'ponto de ônibus','Local onde passageiros aguardam ônibus para transporte público.'),(13,'funcionários treinados','Equipe com conhecimento para atender necessidades específicas dos clientes.'),(14,'filas preferenciais','Áreas reservadas para pessoas com prioridade em serviços de atendimento.'),(15,'banheiro adaptado','Instalação sanitária projetada para acessibilidade de pessoas com deficiência.'),(16,'piso nivelado','Superfície plana, sem desníveis, facilitando a locomoção.'),(17,'área de transferência','Espaço para a mudança de modalidades de transporte.'),(18,'barra sanitária','Dispositivo de apoio em banheiros para auxiliar na higiene pessoal.'),(19,'piso antiderrapante','Revestimento que evita escorregões e quedas.'),(20,'guia rebaixada','Rampa inclinada na calçada para permitir a travessia de cadeiras de rodas.'),(21,'piso não trepidante','Superfície que não vibra ou causa desconforto ao caminhar.');


INSERT INTO myapp_tiposdispositivos (title) VALUES
('bengala'),
('muleta'),
('andador'),
('cadeira de rodas motorizada'),
('cadeiras de rodas manual'),
('cadeira de rodas monobloco'),
('cadeira de rodas dobravel em x'),
('cadeira de rodas com elevação automatica'),
('protese'),
('ortese');

INSERT INTO myapp_tiposlocais (title) VALUES
('igreja'),
('museu'),
('estátua'),
('parque'),
('praia'),
('teatro'),
('biblioteca'),
('monumento'),
('galeria'),
('mercado'),
('jardim botânico'),
('zoológico'),
('catedral'),
('sinagoga'),
('mesquita'),
('castelo'),
('palácio'),
('torre'),
('observatório'),
('planetário'),
('aquário'),
('farol'),
('ilha'),
('praça');