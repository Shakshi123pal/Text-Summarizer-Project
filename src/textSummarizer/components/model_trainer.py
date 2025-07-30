from transformers import AutoModelForSeq2SeqLM, TrainingArguments, Trainer, DataCollatorForSeq2Seq
from transformers import AutoTokenizer
from datasets import load_from_disk,DatasetDict
import os


class ModelTrainer:
    def __init__(self, config):
        self.config = config

    def train(self):
        # ✅ Load full dataset
        dataset = load_from_disk(self.config.data_path)

        # ✅ Load model and tokenizer
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt)
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)

        # ✅ Prepare data collator
        data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=model)
        training_args = TrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=self.config.num_train_epochs,
            warmup_steps=self.config.warmup_steps,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            per_device_eval_batch_size=self.config.per_device_eval_batch_size,
            weight_decay=self.config.weight_decay,
            logging_steps=self.config.logging_steps,
            eval_strategy=self.config.eval_strategy,
            eval_steps=self.config.eval_steps,
            save_total_limit=1,
            report_to="none"
        )

        trainer = Trainer(
            model=model,
            args=training_args,
            tokenizer=tokenizer,
            data_collator=data_collator,
            train_dataset=dataset["train"],
            eval_dataset=dataset["validation"]
        )

        trainer.train()
        model.save_pretrained(os.path.join(self.config.root_dir, "t5-small_model"))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer"))
