import train_vae

train_vae.main(
    train_filepath="./data/splitted_data/tcga_rnaseq_train_fraction_0.9_id_242870585127480531622270373503581547167_seed_42.csv",
    val_filepath="./data/splitted_data/tcga_rnaseq_test_fraction_0.1_id_242870585127480531622270373503581547167_seed_42.csv",
    gene_filepath="./data/2128_genes.pkl",
    model_path="./models/",
    params_filepath="./code/paccmann_omics/examples/gene_expression/example_params.json",
    training_name="pvae",
)
