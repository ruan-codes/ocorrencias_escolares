# Design System AFS

## Identidade

A interface usa a marca da Escola de Educação Profissional Adolfo Ferreira Sousa como base: verde institucional para ações primárias, verde escuro para estados fortes e links, laranja para chamadas de atenção e branco/cinza claro para superfícies administrativas.

## Paleta

- Verde institucional: `#0E8A43`
- Verde escuro: `#0B6B35`
- Verde suave: `#E8F6EE`
- Laranja institucional: `#F29A1F`
- Laranja suave: `#FFF3DF`
- Branco: `#FFFFFF`
- Superfície: `#F5F7FA`
- Bordas: `#E5E7EB`
- Texto principal: `#374151`
- Títulos: `#111827`
- Texto secundário: `#6B7280`
- Erro: `#DC2626`
- Informação: `#2563EB`

## Tipografia

Fonte principal: Inter, com fallback para fontes nativas do sistema. Títulos usam peso 700-800, labels e cabeçalhos de tabela usam peso 700-800, corpo usa peso 400-500.

## Espaçamento e Bordas

- Raio padrão: `8px`
- Layout desktop: conteúdo limitado a `1200px`
- Cards, filtros e tabelas usam borda `#E5E7EB`
- Sombra leve para separar superfícies sem criar efeito pesado

## Componentes

- Botão primário: verde institucional, usado para salvar, filtrar e confirmar ações principais.
- Botão de destaque: laranja institucional, usado para criação de nova ocorrência/aluno.
- Botão secundário: contorno cinza com hover verde suave.
- Inputs: borda cinza, foco verde com halo acessível.
- Tabelas: cabeçalho cinza claro, texto compacto, hover sutil.
- Cards: superfície branca, raio de 8px, sombra leve e borda clara.
- Badges: variações suaves para leve, média e grave.
- Alertas: fundos suaves, contraste alto e ícones.
- Paginação: item ativo em verde institucional.
- Dropdowns: Bootstrap com foco e bordas compatíveis com o tema.
- Modais e toasts: devem seguir o mesmo raio, sombra e paleta dos cards/alertas.

## Responsividade

- Desktop: navegação horizontal, dashboard em cards e painéis lado a lado.
- Tablet: navegação quebra em grade de duas colunas, tabelas continuam responsivas com rolagem horizontal.
- Smartphone: navegação em uma coluna, filtros empilhados, ações agrupadas e tabelas dentro de `.table-responsive`.

## Acessibilidade

- Estados de foco visíveis em botões, links, inputs, selects e paginação.
- Labels visíveis em formulários e labels ocultos acessíveis em filtros compactos.
- Ícones decorativos acompanhados de texto ou `aria-label` quando a ação depende do ícone.
- Cores de status usam texto e contraste, não apenas cor.
