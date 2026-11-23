-- Turn ::: box and ::: hook divs into coloured LaTeX boxes.
-- Build: pandoc memorize.md --lua-filter box.lua --pdf-engine=tectonic -o memorize.pdf
local styles = {
  box  = {'orange!8',  'orange!75!black', 'Formulas for numericals'},
  hook = {'blue!5',    'blue!60!black',   'Hook'},
  map  = {'green!6',   'green!45!black',  'Proof map: the whole proof in one view'},
}

function Div(el)
  for cls, s in pairs(styles) do
    if el.classes:includes(cls) then
      local title = el.attributes.title or s[3]
      return {
        pandoc.RawBlock('latex', '\\begin{tcolorbox}[breakable,colback=' .. s[1]
          .. ',colframe=' .. s[2] .. ',title={' .. title .. '}]'),
        el,
        pandoc.RawBlock('latex', '\\end{tcolorbox}'),
      }
    end
  end
end
