use pyo3::prelude::*;

mod blockchain;
mod dag;

#[pymodule]
#[pyo3(name = "_binaries")]
fn rust(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<blockchain::BlockChain>()?;
    m.add_class::<blockchain::Block>()?;
    m.add_class::<dag::DAG>()?;
    m.add_class::<dag::DAGChain>()?;
    m.add_class::<dag::Transaction>()?;
    Ok(())
}